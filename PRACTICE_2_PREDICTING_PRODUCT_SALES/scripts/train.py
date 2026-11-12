"""Pipeline Lab 2: dự báo doanh thu theo sản phẩm-tháng.

Dữ liệu: UCI Online Retail (ID 352). Target được định nghĩa rõ là tổng
Quantity * UnitPrice theo StockCode và tháng. Đây là bài toán dự báo panel,
không phải dự báo tổng doanh thu toàn cửa hàng.
"""
from __future__ import annotations
import json, logging, warnings
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
FEATURES = ["StockCode", "lag_1", "lag_2", "lag_3", "rolling_mean_3", "month_num"]

def setup():
    for folder in ("outputs/figures", "models", "logs"):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=ROOT / "logs/training.log", level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s")
    logging.info("Bắt đầu pipeline Lab 2")

def load_data():
    """Tải UCI Online Retail và kiểm tra schema bắt buộc."""
    ds = fetch_ucirepo(id=352)
    frame = ds.data.features.copy()
    if ds.data.targets is not None:
        frame = pd.concat([frame, ds.data.targets], axis=1)
    required = {"InvoiceNo", "StockCode", "Quantity", "InvoiceDate", "UnitPrice"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Dataset thiếu cột bắt buộc: {sorted(missing)}")
    return frame

def make_panel(raw):
    """Làm sạch giao dịch, tổng hợp panel đầy đủ và tạo lag không leakage."""
    df = raw.copy()
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    for c in ("Quantity", "UnitPrice"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["StockCode", "InvoiceDate", "Quantity", "UnitPrice"])
    df = df[~df["InvoiceNo"].str.upper().str.startswith("C")]
    df = df[(df.Quantity > 0) & (df.UnitPrice > 0)]
    df["revenue"] = df.Quantity * df.UnitPrice
    df["month"] = df.InvoiceDate.dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby(["StockCode", "month"], as_index=False).revenue.sum()
    months = pd.date_range(monthly.month.min(), monthly.month.max(), freq="MS")
    idx = pd.MultiIndex.from_product([monthly.StockCode.unique(), months],
                                     names=["StockCode", "month"])
    monthly = monthly.set_index(["StockCode", "month"]).reindex(idx, fill_value=0).reset_index()
    monthly = monthly.sort_values(["StockCode", "month"])
    grouped = monthly.groupby("StockCode", sort=False).revenue
    for lag in (1, 2, 3):
        monthly[f"lag_{lag}"] = grouped.shift(lag)
    monthly["rolling_mean_3"] = monthly.groupby("StockCode", sort=False).revenue.transform(
        lambda s: s.shift(1).rolling(3, min_periods=3).mean())
    monthly["month_num"] = monthly.month.dt.month
    # Sắp theo thời gian để TimeSeriesSplit không nhìn thấy tương lai.
    return monthly.dropna(subset=["lag_1", "lag_2", "lag_3"]).sort_values(
        ["month", "StockCode"]).reset_index(drop=True)

def build_pipeline(estimator):
    numeric = ["lag_1", "lag_2", "lag_3", "rolling_mean_3", "month_num"]
    prep = ColumnTransformer([
        ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median"))]), numeric),
        ("product", OneHotEncoder(handle_unknown="ignore"), ["StockCode"]),
    ])
    return Pipeline([("preprocess", prep), ("model", estimator)])

def evaluate(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return {"MAE": float(mean_absolute_error(y_true, y_pred)),
            "MSE": float(mse), "RMSE": float(np.sqrt(mse)),
            "R2": float(r2_score(y_true, y_pred)) if len(y_true) > 1 else None}

def save_figures(test, pred, comparison, best_pipe):
    out = ROOT / "outputs/figures"
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(test.revenue, pred, alpha=.25)
    hi = max(float(test.revenue.max()), float(np.max(pred)))
    ax.plot([0, hi], [0, hi], "k--")
    ax.set(title="Doanh thu thực tế và dự báo", xlabel="Thực tế (GBP)", ylabel="Dự báo (GBP)")
    fig.tight_layout(); fig.savefig(out / "actual_vs_predicted.png", dpi=160); plt.close(fig)
    residual = test.revenue.to_numpy() - pred
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(pred, residual, alpha=.25); ax.axhline(0, color="black", linestyle="--")
    ax.set(title="Residual plot", xlabel="Giá trị dự báo (GBP)", ylabel="Sai số (thực tế - dự báo)")
    fig.tight_layout(); fig.savefig(out / "residuals.png", dpi=160); plt.close(fig)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(comparison.model, comparison.RMSE); ax.tick_params(axis="x", rotation=20)
    ax.set(title="So sánh mô hình trên tập test", ylabel="RMSE (GBP)")
    fig.tight_layout(); fig.savefig(out / "model_comparison.png", dpi=160); plt.close(fig)
    try:
        names = best_pipe.named_steps["preprocess"].get_feature_names_out()
        values = best_pipe.named_steps["model"].feature_importances_
        imp = pd.DataFrame({"feature": names, "importance": values}).nlargest(20, "importance")
        imp.to_csv(ROOT / "outputs/feature_importance.csv", index=False)
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.barh(imp.feature[::-1], imp.importance[::-1])
        ax.set(title="Top 20 đặc trưng quan trọng", xlabel="Feature importance")
        fig.tight_layout(); fig.savefig(out / "feature_importance.png", dpi=160); plt.close(fig)
    except (AttributeError, ValueError):
        logging.info("Mô hình tốt nhất không cung cấp feature_importances_.")

def main():
    setup()
    raw = load_data()
    raw_summary = {"rows_downloaded": int(len(raw)), "columns": list(raw.columns)}
    panel = make_panel(raw)
    if panel.empty: raise ValueError("Không có dữ liệu sau tạo lag.")
    months = np.sort(panel.month.unique())
    if len(months) < 8: raise ValueError("Cần tối thiểu 8 tháng sau xử lý để train/test và CV.")
    split_idx = max(1, int(len(months) * .8))
    test_start = months[split_idx]
    train, test = panel[panel.month < test_start].copy(), panel[panel.month >= test_start].copy()
    if train.empty or test.empty: raise ValueError("Train/test rỗng.")
    X_train, y_train = train[FEATURES], train.revenue
    X_test, y_test = test[FEATURES], test.revenue
    candidates = {
        "Linear Regression": build_pipeline(LinearRegression()),
        "Decision Tree": build_pipeline(DecisionTreeRegressor(random_state=SEED)),
        "Random Forest": build_pipeline(RandomForestRegressor(random_state=SEED, n_jobs=-1)),
        "Gradient Boosting": build_pipeline(GradientBoostingRegressor(random_state=SEED)),
    }
    rows, fitted = [], {}
    for name, pipe in candidates.items():
        pipe.fit(X_train, y_train)
        fitted[name] = pipe
        rows.append({"model": name, **evaluate(y_test, np.maximum(0, pipe.predict(X_test))),
                     "tuned": False})
    # Tuning chỉ trên train; test không tham gia chọn tham số.
    n_splits = min(4, max(2, len(np.unique(train.month)) // 3))
    month_cv = TimeSeriesSplit(n_splits=n_splits)
    train_months = np.sort(train.month.unique())
    # Mỗi fold chia theo tháng hoàn chỉnh, không cắt một tháng thành train/validation.
    cv = [(np.flatnonzero(train.month.isin(train_months[tr_idx])),
           np.flatnonzero(train.month.isin(train_months[va_idx])))
          for tr_idx, va_idx in month_cv.split(train_months)]
    search = RandomizedSearchCV(
        build_pipeline(RandomForestRegressor(random_state=SEED, n_jobs=-1)),
        {"model__n_estimators": [150, 250, 400],
         "model__max_depth": [8, 12, 18, None],
         "model__min_samples_leaf": [1, 2, 4, 6],
         "model__max_features": [0.6, 0.8, 1.0]},
        n_iter=12, scoring="neg_root_mean_squared_error", cv=cv,
        random_state=SEED, n_jobs=-1, verbose=0)
    search.fit(X_train, y_train)
    tuned = search.best_estimator_
    tuned_pred = np.maximum(0, tuned.predict(X_test))
    rows.append({"model": "Random Forest (tuned)", **evaluate(y_test, tuned_pred), "tuned": True})
    fitted["Random Forest (tuned)"] = tuned
    comparison = pd.DataFrame(rows).sort_values("RMSE").reset_index(drop=True)
    comparison.to_csv(ROOT / "outputs/model_comparison.csv", index=False)
    best_name = str(comparison.iloc[0].model)
    best_pipe = fitted[best_name]
    pred = np.maximum(0, best_pipe.predict(X_test))
    artifact = {"pipeline": best_pipe, "model_name": best_name, "features": FEATURES,
                "target": "monthly_revenue_gbp", "dataset": "UCI Online Retail (ID 352)",
                "test_start": str(pd.Timestamp(test_start).date())}
    joblib.dump(artifact, ROOT / "models/best_model.joblib")
    result = test[["StockCode", "month", "revenue"]].copy()
    result["predicted_revenue"] = pred
    result["residual"] = result.revenue - result.predicted_revenue
    result.to_csv(ROOT / "outputs/test_predictions.csv", index=False)
    save_figures(test, pred, comparison, best_pipe)
    report = {"dataset": raw_summary, "panel_rows": int(len(panel)),
              "train_rows": int(len(train)), "test_rows": int(len(test)),
              "train_months": [str(pd.Timestamp(x).date()) for x in np.sort(train.month.unique())],
              "test_start": str(pd.Timestamp(test_start).date()), "best_model": best_name,
              "best_params": search.best_params_, "metrics": comparison.to_dict("records"),
              "notes": ["Holdout theo thời gian; không shuffle.",
                        "Lag và rolling mean chỉ sử dụng các tháng trước.",
                        "RMSE/MAE/R2 được tính trên target gốc GBP.",
                        "Không diễn giải R2 âm là lỗi chạy; có thể mô hình kém baseline trung bình."]}
    (ROOT / "outputs/metrics.json").write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    logging.info("Hoàn tất; best=%s; metrics=%s", best_name, report["metrics"])
    print(comparison.to_string(index=False))
    print(f"Best model: {best_name}; test bắt đầu: {test_start}")

if __name__ == "__main__":
    main()

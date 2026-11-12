"""Huấn luyện và đánh giá mô hình dự báo doanh thu tháng theo sản phẩm."""
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

ROOT = Path(__file__).resolve().parents[1]
for name in ("outputs", "models", "logs"):
    (ROOT / name).mkdir(exist_ok=True)


def load_data():
    """Tải dataset Online Retail ID 352 từ UCI."""
    dataset = fetch_ucirepo(id=352)
    frame = dataset.data.features.copy()
    if dataset.data.targets is not None:
        frame = pd.concat([frame, dataset.data.targets], axis=1)
    required = {"InvoiceNo", "StockCode", "Quantity", "InvoiceDate", "UnitPrice"}
    if not required.issubset(frame.columns):
        raise ValueError(f"Thiếu cột: {sorted(required - set(frame.columns))}")
    return frame


def make_panel(raw):
    """Tổng hợp doanh thu tháng; tạo lag chỉ từ lịch sử."""
    df = raw.copy()
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    for col in ("Quantity", "UnitPrice"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["StockCode", "InvoiceDate", "Quantity", "UnitPrice"])
    df = df[~df["InvoiceNo"].str.upper().str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df["revenue"] = df["Quantity"] * df["UnitPrice"]
    df["month"] = df["InvoiceDate"].dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby(["StockCode", "month"], as_index=False)["revenue"].sum()
    products = monthly["StockCode"].unique()
    months = pd.date_range(monthly["month"].min(), monthly["month"].max(), freq="MS")
    idx = pd.MultiIndex.from_product([products, months], names=["StockCode", "month"])
    monthly = monthly.set_index(["StockCode", "month"]).reindex(idx, fill_value=0).reset_index()
    monthly = monthly.sort_values(["StockCode", "month"])
    for lag in (1, 2, 3):
        monthly[f"lag_{lag}"] = monthly.groupby("StockCode")["revenue"].shift(lag)
    monthly["rolling_mean_3"] = monthly.groupby("StockCode")["revenue"].transform(
        lambda s: s.shift(1).rolling(3, min_periods=1).mean())
    monthly["month_num"] = monthly["month"].dt.month
    return monthly.dropna(subset=["lag_1", "lag_2", "lag_3"])


def build_pipeline(model):
    numeric = ["lag_1", "lag_2", "lag_3", "rolling_mean_3", "month_num"]
    prep = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), numeric),
        ("product", OneHotEncoder(handle_unknown="ignore"), ["StockCode"]),
    ])
    return Pipeline([("preprocess", prep), ("model", model)])


def main():
    panel = make_panel(load_data())
    if panel.empty:
        raise ValueError("Không có đủ dữ liệu sau khi tạo lag.")
    months = np.sort(panel["month"].unique())
    if len(months) < 5:
        raise ValueError("Cần ít nhất 5 tháng có dữ liệu để tạo train/test theo thời gian.")
    test_start = months[max(1, int(len(months) * .8))]
    train, test = panel[panel.month < test_start], panel[panel.month >= test_start]
    if train.empty or test.empty:
        raise ValueError("Train hoặc test rỗng; kiểm tra dữ liệu.")
    cols = ["StockCode", "lag_1", "lag_2", "lag_3", "rolling_mean_3", "month_num"]
    X_train, X_test = train[cols], test[cols]
    y_train, y_test = train.revenue, test.revenue
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(max_depth=8, min_samples_leaf=5, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=200, max_depth=12, min_samples_leaf=3, n_jobs=-1, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=120, learning_rate=.04, max_depth=2, loss="huber", random_state=42),
    }
    rows, fitted = [], {}
    for name, model in models.items():
        pipe = build_pipeline(model)
        pipe.fit(X_train, y_train)
        pred = np.maximum(0, pipe.predict(X_test))
        mse = mean_squared_error(y_test, pred)
        rows.append({"model": name, "MAE": mean_absolute_error(y_test, pred),
                     "MSE": mse, "RMSE": mse ** .5, "R2": r2_score(y_test, pred)})
        fitted[name] = pipe
    comparison = pd.DataFrame(rows).sort_values("RMSE")
    comparison.to_csv(ROOT / "outputs/model_comparison.csv", index=False)
    best = comparison.iloc[0]["model"]
    joblib.dump({"pipeline": fitted[best], "model_name": best, "features": cols},
                ROOT / "models/best_model.joblib")
    pred = np.maximum(0, fitted[best].predict(X_test))
    result = test[["StockCode", "month", "revenue"]].copy()
    result["predicted_revenue"] = pred
    result.to_csv(ROOT / "outputs/test_predictions.csv", index=False)
    (ROOT / "outputs/metrics.json").write_text(json.dumps({
        "best_model": best, "test_start": str(pd.Timestamp(test_start).date()),
        "train_rows": len(train), "test_rows": len(test),
        "metrics": comparison.to_dict(orient="records")
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(y_test, pred, alpha=.25)
    upper = max(float(y_test.max()), float(pred.max()))
    ax.plot([0, upper], [0, upper], "--")
    ax.set(title=f"Thực tế và dự báo — {best}", xlabel="Doanh thu thực tế (GBP)", ylabel="Doanh thu dự báo (GBP)")
    fig.tight_layout(); fig.savefig(ROOT / "outputs/actual_vs_predicted.png", dpi=150); plt.close(fig)
    print(comparison.to_string(index=False))
    print(f"Best model: {best}; test bắt đầu từ {test_start}")


if __name__ == "__main__":
    main()

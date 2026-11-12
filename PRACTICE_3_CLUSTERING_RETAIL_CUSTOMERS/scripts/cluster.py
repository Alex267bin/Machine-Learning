"""So sánh K-Means, K-Medoids, DBSCAN và Hierarchical clustering."""
from pathlib import Path
import argparse
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

ROOT = Path(__file__).resolve().parents[1]


def load_data(path):
    """Đọc và chuẩn hóa tên cột Mall Customers."""
    df = pd.read_csv(path)
    df = df.rename(columns={
        "Annual Income (k$)": "Annual Income",
        "Annual Income (K$)": "Annual Income",
        "Spending Score (1-100)": "Spending Score",
        "Spending Score (1–100)": "Spending Score",
    })
    required = {"Gender", "Age", "Annual Income", "Spending Score"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Thiếu cột {sorted(missing)}; hiện có {list(df.columns)}")
    for col in ("Age", "Annual Income", "Spending Score"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Gender", "Age", "Annual Income", "Spending Score"]).drop_duplicates()
    if len(df) < 4:
        raise ValueError("Không đủ quan sát hợp lệ.")
    return df


def transform(df):
    """Bỏ ID; one-hot Gender và chuẩn hóa các biến số."""
    numeric = ["Age", "Annual Income", "Spending Score"]
    prep = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())]), numeric),
        ("gender", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                             ("onehot", OneHotEncoder(handle_unknown="ignore"))]), ["Gender"]),
    ])
    return prep.fit_transform(df)


def clustering_metrics(X, labels):
    """Tính metric sau khi loại noise; trả NaN nếu điều kiện không hợp lệ."""
    labels = np.asarray(labels)
    mask = labels != -1
    X_valid, y_valid = X[mask], labels[mask]
    k = len(np.unique(y_valid))
    if k < 2 or k >= len(y_valid):
        return {"silhouette": np.nan, "davies_bouldin": np.nan, "calinski_harabasz": np.nan}
    return {
        "silhouette": silhouette_score(X_valid, y_valid),
        "davies_bouldin": davies_bouldin_score(X_valid, y_valid),
        "calinski_harabasz": calinski_harabasz_score(X_valid, y_valid),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default=str(ROOT / "data/Mall_Customers.csv"))
    args = parser.parse_args()
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    df = load_data(args.data)
    X = transform(df)
    X_dense = X.toarray() if hasattr(X, "toarray") else X

    # Elbow và Silhouette dùng để khảo sát k cho K-Means.
    ks = range(2, min(11, len(df)))
    elbow, silhouette = [], []
    for k in ks:
        model = KMeans(n_clusters=k, n_init=20, random_state=42).fit(X)
        elbow.append({"k": k, "inertia": model.inertia_})
        silhouette.append({"k": k, "silhouette": silhouette_score(X, model.labels_)})
    pd.DataFrame(elbow).to_csv(out / "elbow_values.csv", index=False)
    pd.DataFrame(silhouette).to_csv(out / "silhouette_by_k.csv", index=False)
    best_k = max(silhouette, key=lambda row: row["silhouette"])["k"]

    fig, ax = plt.subplots()
    ax.plot([r["k"] for r in elbow], [r["inertia"] for r in elbow], marker="o")
    ax.set(title="Elbow — K-Means", xlabel="Số cụm k", ylabel="Inertia")
    fig.tight_layout(); fig.savefig(out / "elbow.png", dpi=150); plt.close(fig)

    models = {
        "K-Means": KMeans(n_clusters=best_k, n_init=20, random_state=42),
        "DBSCAN": DBSCAN(eps=0.8, min_samples=5),
        "Hierarchical": AgglomerativeClustering(n_clusters=best_k, linkage="ward"),
    }
    try:
        from sklearn_extra.cluster import KMedoids
        models["K-Medoids"] = KMedoids(n_clusters=best_k, metric="euclidean", random_state=42)
    except Exception as exc:
        warnings.warn(f"Không chạy được K-Medoids do dependency: {exc}")

    records, label_map = [], {}
    for name, model in models.items():
        labels = model.fit_predict(X)
        label_map[name] = labels
        records.append({"model": name, "cluster_count": len(set(labels) - {-1}),
                        "noise_count": int(np.sum(np.asarray(labels) == -1)),
                        **clustering_metrics(X, labels)})
    pd.DataFrame(records).to_csv(out / "metrics.csv", index=False)

    # Profile và diễn giải cluster K-Means dựa trên dữ liệu thực.
    result = df.copy()
    result["Cluster"] = label_map["K-Means"]
    result.to_csv(out / "customer_clusters.csv", index=False)
    profile = result.groupby("Cluster").agg(
        customer_count=("Cluster", "size"), mean_age=("Age", "mean"),
        mean_income=("Annual Income", "mean"), mean_spending=("Spending Score", "mean"))
    gender_share = pd.crosstab(result["Cluster"], result["Gender"], normalize="index").add_prefix("gender_share_")
    profile.join(gender_share).to_csv(out / "cluster_profiles.csv")

    coords = PCA(n_components=2, random_state=42).fit_transform(X_dense)
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(coords[:, 0], coords[:, 1], c=label_map["K-Means"], cmap="tab10", alpha=.8)
    ax.set(title="Phân cụm khách hàng — PCA 2D", xlabel="Thành phần chính 1", ylabel="Thành phần chính 2")
    fig.colorbar(scatter, ax=ax, label="Cluster")
    fig.tight_layout(); fig.savefig(out / "pca_clusters.png", dpi=150); plt.close(fig)

    try:
        from scipy.cluster.hierarchy import linkage, dendrogram
        Z = linkage(X_dense[:min(100, len(X_dense))], method="ward")
        fig, ax = plt.subplots(figsize=(12, 5))
        dendrogram(Z, no_labels=True, ax=ax)
        ax.set(title="Dendrogram — Ward linkage (tối đa 100 quan sát)", xlabel="Quan sát", ylabel="Khoảng cách")
        fig.tight_layout(); fig.savefig(out / "dendrogram.png", dpi=150); plt.close(fig)
    except Exception as exc:
        warnings.warn(f"Không tạo được dendrogram: {exc}")

    print(pd.DataFrame(records).to_string(index=False))
    print("\nProfile K-Means:\n", profile.round(2).to_string())


if __name__ == "__main__":
    main()

"""Pipeline Lab 3: phân cụm khách hàng và so sánh bốn thuật toán.

K-Medoids được cài đặt bằng PAM đơn giản để tránh phụ thuộc scikit-learn-extra,
vốn có thể khó cài trên Python mới. Mọi profile đều lấy từ dữ liệu gốc.
"""
from __future__ import annotations
import json, logging, argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from scipy.cluster.hierarchy import linkage, dendrogram

ROOT = Path(__file__).resolve().parents[1]
SEED = 42

def load_data(path):
    df = pd.read_csv(path)
    df = df.rename(columns={"Annual Income (k$)": "Annual Income",
        "Annual Income (K$)": "Annual Income", "Spending Score (1-100)": "Spending Score",
        "Spending Score (1–100)": "Spending Score"})
    required = {"Gender", "Age", "Annual Income", "Spending Score"}
    missing = required - set(df.columns)
    if missing: raise ValueError(f"Thiếu cột {sorted(missing)}; hiện có {list(df.columns)}")
    for col in ("Age", "Annual Income", "Spending Score"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    before = len(df)
    df = df.dropna(subset=list(required)).drop_duplicates().reset_index(drop=True)
    if len(df) < 5: raise ValueError("Không đủ quan sát hợp lệ.")
    logging.info("Dữ liệu: %s dòng; loại %s dòng thiếu/trùng.", len(df), before-len(df))
    return df

def transform(df):
    """Scale numerical features; encode Gender; không dùng CustomerID."""
    numeric = ["Age", "Annual Income", "Spending Score"]
    prep = ColumnTransformer([
        ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")),
                              ("scaler", StandardScaler())]), numeric),
        ("gender", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                             ("onehot", OneHotEncoder(handle_unknown="ignore"))]), ["Gender"])
    ])
    return prep.fit_transform(df)

def pam_kmedoids(X, k, max_iter=100, seed=SEED):
    """PAM (Partitioning Around Medoids), khoảng cách Euclidean."""
    X = np.asarray(X, dtype=float)
    rng = np.random.default_rng(seed)
    n = len(X)
    if k < 2 or k >= n: raise ValueError("k phải nằm trong [2, n-1].")
    # Ma trận khoảng cách n*n phù hợp dataset Mall nhỏ; giới hạn để tránh cấp phát lớn.
    if n > 5000: raise ValueError("PAM bản đầy đủ giới hạn 5.000 dòng do ma trận khoảng cách.")
    distances = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2))
    medoids = rng.choice(n, size=k, replace=False)
    for _ in range(max_iter):
        costs = distances[:, medoids]
        labels = costs.argmin(axis=1)
        current = costs.min(axis=1).sum()
        best_cost, best = current, medoids.copy()
        for slot in range(k):
            for candidate in range(n):
                if candidate in medoids: continue
                trial = medoids.copy(); trial[slot] = candidate
                cost = distances[:, trial].min(axis=1).sum()
                if cost + 1e-9 < best_cost:
                    best_cost, best = cost, trial
        if np.array_equal(best, medoids): break
        medoids = best
    labels = distances[:, medoids].argmin(axis=1)
    return labels, medoids

def valid_metrics(X, labels):
    labels = np.asarray(labels)
    mask = labels != -1
    Xv, yv = np.asarray(X)[mask], labels[mask]
    clusters = np.unique(yv)
    if len(clusters) < 2 or len(clusters) >= len(yv):
        return {"silhouette": None, "davies_bouldin": None,
                "calinski_harabasz": None, "metric_samples": int(len(yv))}
    return {"silhouette": float(silhouette_score(Xv, yv)),
            "davies_bouldin": float(davies_bouldin_score(Xv, yv)),
            "calinski_harabasz": float(calinski_harabasz_score(Xv, yv)),
            "metric_samples": int(len(yv))}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default=str(ROOT / "data/Mall_Customers.csv"))
    parser.add_argument("--eps", type=float, default=0.75)
    parser.add_argument("--min-samples", type=int, default=5)
    args = parser.parse_args()
    out = ROOT / "outputs"; figs = out / "figures"
    for p in (out, figs, ROOT / "logs"): p.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=ROOT / "logs/clustering.log", level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s")
    df = load_data(args.data)
    Xsp = transform(df); X = Xsp.toarray() if hasattr(Xsp, "toarray") else np.asarray(Xsp)
    max_k = min(10, len(df)-1)
    ks = range(2, max_k+1)
    elbow, sil = [], []
    for k in ks:
        km = KMeans(n_clusters=k, n_init=20, random_state=SEED).fit(X)
        elbow.append({"k": k, "inertia": float(km.inertia_)})
        sil.append({"k": k, "silhouette": float(silhouette_score(X, km.labels_))})
    pd.DataFrame(elbow).to_csv(out/"elbow_values.csv", index=False)
    pd.DataFrame(sil).to_csv(out/"silhouette_by_k.csv", index=False)
    best_k = max(sil, key=lambda r:r["silhouette"])["k"]
    fig, ax = plt.subplots(); ax.plot([r["k"] for r in elbow], [r["inertia"] for r in elbow], marker="o")
    ax.set(title="Elbow method", xlabel="Số cụm k", ylabel="Inertia")
    fig.tight_layout(); fig.savefig(figs/"elbow.png", dpi=160); plt.close(fig)
    fig, ax = plt.subplots(); ax.plot([r["k"] for r in sil], [r["silhouette"] for r in sil], marker="o")
    ax.set(title="Silhouette theo k", xlabel="Số cụm k", ylabel="Silhouette")
    fig.tight_layout(); fig.savefig(figs/"silhouette_by_k.png", dpi=160); plt.close(fig)
    models = {}
    km = KMeans(n_clusters=best_k, n_init=20, random_state=SEED)
    models["K-Means"] = (km.fit_predict(X), {"k": best_k})
    med_labels, medoids = pam_kmedoids(X, best_k)
    models["K-Medoids"] = (med_labels, {"k": best_k, "medoid_indices": medoids.tolist()})
    db = DBSCAN(eps=args.eps, min_samples=args.min_samples)
    models["DBSCAN"] = (db.fit_predict(X), {"eps": args.eps, "min_samples": args.min_samples})
    hier = AgglomerativeClustering(n_clusters=best_k, linkage="ward")
    models["Hierarchical"] = (hier.fit_predict(X), {"k": best_k, "linkage": "ward"})
    records = []
    for name, (labels, params) in models.items():
        row = {"model": name, "cluster_count": int(len(set(labels)-{-1})),
               "noise_count": int(np.sum(np.asarray(labels)==-1)), **valid_metrics(X, labels),
               "parameters": json.dumps(params, ensure_ascii=False)}
        records.append(row)
    pd.DataFrame(records).to_csv(out/"metrics.csv", index=False)
    # Thử nhiều eps DBSCAN để không kết luận từ một tham số duy nhất.
    eps_rows = []
    for eps in np.arange(0.3, 1.51, 0.1):
        labels = DBSCAN(eps=float(eps), min_samples=args.min_samples).fit_predict(X)
        eps_rows.append({"eps": round(float(eps),2),
                         "clusters": int(len(set(labels)-{-1})),
                         "noise": int(np.sum(labels==-1)), **valid_metrics(X, labels)})
    pd.DataFrame(eps_rows).to_csv(out/"dbscan_parameter_sweep.csv", index=False)
    # Lưu nhãn từng thuật toán để đối chiếu, không chỉ riêng K-Means.
    assignments = df.copy()
    for name, (labels, _) in models.items():
        assignments[name.replace("-", "_").replace(" ", "_")+"_cluster"] = labels
    assignments.to_csv(out/"customer_cluster_assignments.csv", index=False)
    # Profile dựa trên K-Means và dữ liệu gốc, không gán persona tự động.
    profile_data = df.copy(); profile_data["Cluster"] = models["K-Means"][0]
    profile = profile_data.groupby("Cluster").agg(customer_count=("Cluster","size"),
        mean_age=("Age","mean"), median_age=("Age","median"),
        mean_income=("Annual Income","mean"), median_income=("Annual Income","median"),
        mean_spending=("Spending Score","mean"), median_spending=("Spending Score","median"))
    gender = pd.crosstab(profile_data.Cluster, profile_data.Gender, normalize="index").add_prefix("gender_share_")
    profile.join(gender).to_csv(out/"cluster_profiles.csv")
    coords = PCA(n_components=2, random_state=SEED).fit_transform(X)
    fig, ax = plt.subplots(figsize=(8,6))
    sc=ax.scatter(coords[:,0], coords[:,1], c=models["K-Means"][0], cmap="tab10", alpha=.85)
    ax.set(title="K-Means clusters trên PCA 2D", xlabel="Principal component 1", ylabel="Principal component 2")
    fig.colorbar(sc, ax=ax, label="Cluster"); fig.tight_layout()
    fig.savefig(figs/"pca_clusters.png", dpi=160); plt.close(fig)
    # Dendrogram có giới hạn quan sát để hình dễ đọc.
    sample = X[:min(100, len(X))]
    Z = linkage(sample, method="ward")
    fig, ax = plt.subplots(figsize=(12,5)); dendrogram(Z, no_labels=True, ax=ax)
    ax.set(title=f"Dendrogram Ward (tối đa {len(sample)} quan sát)", xlabel="Quan sát", ylabel="Khoảng cách")
    fig.tight_layout(); fig.savefig(figs/"dendrogram.png", dpi=160); plt.close(fig)
    report = {"rows_used": int(len(df)), "features_used": ["Age","Annual Income","Spending Score","Gender"],
              "scaling": "StandardScaler cho biến số; OneHotEncoder cho Gender",
              "selected_k_by_silhouette": int(best_k), "algorithms": records,
              "dbscan_eps_sweep": eps_rows,
              "metric_note": "DBSCAN tính metric sau khi loại noise (-1); metric_samples được ghi rõ. So sánh cần lưu ý khác tập mẫu.",
              "interpretation_note": "Chỉ profile theo số liệu thống kê; không gán tên persona khi chưa phân tích bằng chứng."}
    (out/"clustering_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    logging.info("Hoàn tất clustering; k=%s; metrics=%s", best_k, records)
    print(pd.DataFrame(records).to_string(index=False))
    print("\nProfile K-Means:\n", profile.round(2).to_string())

if __name__ == "__main__":
    main()

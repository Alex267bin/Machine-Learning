"""K-Means Image Segmentation trên không gian màu RGB của từng pixel."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
from PIL import Image, UnidentifiedImageError
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

ROOT = Path(__file__).resolve().parents[1]

def segment(path, k=5, max_side=600):
    """Load -> RGB -> resize -> flatten -> K-Means -> thay pixel bằng centroid."""
    image_path = Path(path).expanduser()
    if not image_path.is_file():
        raise FileNotFoundError(f"Không tìm thấy ảnh: {image_path}")
    if k < 2:
        raise ValueError("k phải >= 2.")
    if max_side < 16:
        raise ValueError("max_side phải >= 16 pixel.")
    try:
        image = Image.open(image_path).convert("RGB")
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError(f"Không đọc được file ảnh hợp lệ: {image_path}") from exc
    image.thumbnail((max_side, max_side))
    original = np.asarray(image, dtype=np.uint8)
    pixels = original.reshape(-1, 3).astype(np.float32)
    if len(pixels) < k:
        raise ValueError(f"Ảnh chỉ có {len(pixels)} pixel; cần ít nhất k={k}.")
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = model.fit_predict(pixels)
    # Mỗi pixel được thay bằng màu centroid của cụm tương ứng.
    compressed = np.rint(model.cluster_centers_[labels]).clip(0, 255).astype(np.uint8)
    return original, compressed.reshape(original.shape), model

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True, help="Đường dẫn ảnh đầu vào.")
    parser.add_argument("--k", type=int, default=5, help="Số màu đại diện (>=2).")
    parser.add_argument("--max-side", type=int, default=600, help="Giới hạn cạnh dài để giảm thời gian.")
    args = parser.parse_args()
    try:
        original, segmented, model = segment(args.image, args.k, args.max_side)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    out = ROOT / "outputs"
    figs = out / "figures"
    figs.mkdir(parents=True, exist_ok=True)
    Image.fromarray(segmented).save(out / "segmented_image.png")
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    axes[0].imshow(original); axes[0].set_title("Ảnh gốc (đã resize)"); axes[0].axis("off")
    axes[1].imshow(segmented); axes[1].set_title(f"K-Means Image Segmentation (k={args.k})"); axes[1].axis("off")
    fig.tight_layout(); fig.savefig(figs / "image_segmentation_comparison.png", dpi=160); plt.close(fig)
    print(f"Kích thước xử lý: {original.shape[1]}x{original.shape[0]}")
    print(f"Số màu đại diện: {len(model.cluster_centers_)}")
    print(f"Ảnh kết quả: {out / 'segmented_image.png'}")
    print(f"Biểu đồ so sánh: {figs / 'image_segmentation_comparison.png'}")

if __name__ == "__main__":
    main()

"""Phân đoạn ảnh bằng K-Means trên vector màu RGB của từng pixel."""
import argparse
from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def segment(path, k=5, max_side=600):
    """Đọc ảnh, gom cụm pixel theo màu, thay pixel bằng centroid."""
    image = Image.open(path).convert("RGB")
    image.thumbnail((max_side, max_side))
    original = np.asarray(image)
    pixels = original.reshape(-1, 3).astype(np.float32)
    if len(pixels) < k:
        raise ValueError("Số pixel nhỏ hơn k.")
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = model.fit_predict(pixels)
    reduced = model.cluster_centers_[labels].clip(0, 255).astype(np.uint8)
    return original, reduced.reshape(original.shape)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()
    if args.k < 2:
        parser.error("--k phải >= 2")
    original, segmented = segment(args.image, args.k)
    out = Path(__file__).resolve().parents[1] / "outputs"
    out.mkdir(exist_ok=True)
    Image.fromarray(segmented).save(out / "segmented_image.png")
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original); axes[0].set_title("Ảnh gốc"); axes[0].axis("off")
    axes[1].imshow(segmented); axes[1].set_title(f"K-Means Image Segmentation (k={args.k})"); axes[1].axis("off")
    fig.tight_layout(); fig.savefig(out / "image_segmentation_comparison.png", dpi=150); plt.close(fig)
    print(f"Đã lưu kết quả tại {out}")


if __name__ == "__main__":
    main()

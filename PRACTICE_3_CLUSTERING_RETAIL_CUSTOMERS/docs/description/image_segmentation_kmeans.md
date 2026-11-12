# K-Means Image Segmentation (RGB Color Quantization)

## Purpose
Reduce the number of distinct colors in an image by grouping pixels with similar RGB values.

## Input
An image file readable by Pillow. It is converted to RGB and resized so its longest side does not exceed max_side (default 600).

## Output
A segmented image and side-by-side comparison figure. Each pixel is replaced by the RGB centroid of its assigned cluster.

## How it works
The image is reshaped into an N × 3 matrix, where each row is one pixel's red, green and blue values. K-Means groups these vectors into k clusters. The centroid color replaces each original pixel.

## Parameters
Default k=5, max_side=600, n_init=10 and random_state=42. The script validates the image, k and pixel count.

## Strengths and limitations
Simple demonstration of clustering and color quantization. It does not understand objects, boundaries or semantic classes; it is not semantic segmentation. Results depend on k and RGB Euclidean distance.

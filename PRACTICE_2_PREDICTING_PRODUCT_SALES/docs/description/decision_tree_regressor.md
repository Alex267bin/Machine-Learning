# Decision Tree Regressor

## Purpose
Model nonlinear relationships and feature interactions for product-month revenue forecasting.

## Input / Output
Uses the shared Lab 2 feature pipeline; outputs a continuous non-negative revenue estimate after prediction clipping.

## How it works
The tree recursively partitions feature space using thresholds that reduce within-node squared error. A leaf predicts the average target of its training observations.

## Evaluation
Compared using training-only temporal CV RMSE and chronological holdout MAE, MSE, RMSE and R².

## Strengths and limitations
Captures nonlinear rules and is easy to visualize conceptually. A deep tree can overfit and be unstable to small data changes. The current baseline sets random_state but does not tune tree depth.

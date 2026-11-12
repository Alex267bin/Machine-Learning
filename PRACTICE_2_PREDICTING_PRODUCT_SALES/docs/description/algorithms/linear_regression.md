# Linear Regression

## Purpose
A simple supervised regression baseline that models a linear relationship between input features and monthly product revenue.

## Input
The pipeline receives StockCode, three previous-month revenue lags, a shifted three-month rolling mean, and calendar month number. StockCode is one-hot encoded; numeric features are median-imputed.

## Output
A continuous predicted monthly revenue in GBP. Negative predictions are clipped to zero before evaluation/output.

## How it works
The estimator learns coefficients by minimizing the sum of squared residuals. The fitted coefficients describe the model's linear association with encoded product and temporal features.

## Evaluation
MAE, MSE, RMSE and R² on the chronological holdout; CV RMSE on training folds.

## Strengths and limitations
Fast and interpretable baseline. It may underfit nonlinear trends, interactions and abrupt changes. Coefficients are associations, not causal effects.

# Decision Tree Regressor

**Purpose:** learn nonlinear rules for product-month revenue.

**Input:** StockCode, lag_1, lag_2, lag_3, rolling_mean_3 and month_num. StockCode is one-hot encoded; numeric features are median-imputed.

**Output:** continuous predicted monthly revenue in GBP; predictions are clipped at zero before reporting.

**How it works:** recursively split feature space at thresholds that reduce squared error. Each leaf predicts the mean target of its training rows.

**Evaluation:** training-only temporal CV RMSE and chronological holdout MAE, MSE, RMSE and R².

**Strengths / limitations:** captures nonlinear rules and interactions; can overfit and is sensitive to data changes. This script sets random_state but does not tune tree depth.
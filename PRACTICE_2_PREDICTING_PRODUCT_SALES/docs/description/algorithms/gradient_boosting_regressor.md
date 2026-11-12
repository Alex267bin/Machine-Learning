# Gradient Boosting Regressor

**Purpose:** boosted-tree candidate for monthly product revenue forecasting.

**Input / output:** shared Lab 2 preprocessing and features; continuous monthly revenue estimate in GBP.

**How it works:** adds trees sequentially; each tree fits remaining prediction errors, with its contribution controlled by a learning rate.

**Evaluation:** same training-only temporal CV RMSE and chronological holdout regression metrics as other candidates.

**Strengths / limitations:** models nonlinear patterns effectively, but can overfit and depends on tree and learning-rate settings. The current script uses estimator defaults apart from random_state; it does not tune this model separately.
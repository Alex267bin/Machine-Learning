# Random Forest Regressor

**Purpose:** ensemble decision trees for nonlinear product-month revenue prediction.

**Input / output:** the shared Lab 2 features and preprocessing pipeline; output is predicted monthly revenue in GBP.

**How it works:** trains many trees with bootstrap sampling and randomized feature selection, then averages their predictions to reduce variance.

**Tuning:** RandomizedSearchCV searches n_estimators, max_depth, min_samples_leaf and max_features using chronological month-based folds from training data only.

**Evaluation:** CV RMSE selects the model; holdout MAE, MSE, RMSE and R² are reported separately. Feature importance is saved only when the selected tree model supports it.

**Strengths / limitations:** models nonlinearities and interactions, but is less interpretable and more computationally expensive than a linear baseline. Feature importance is not causal.
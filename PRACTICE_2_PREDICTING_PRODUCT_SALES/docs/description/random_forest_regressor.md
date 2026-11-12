# Random Forest Regressor

## Purpose
Ensemble of decision trees for nonlinear product-month revenue prediction.

## Input / Output
Uses the common preprocessing pipeline and Lab 2 features. Output is a continuous monthly revenue estimate in GBP.

## How it works
Many decision trees are trained on bootstrap samples with randomized feature selection. Their predictions are averaged to reduce variance compared with a single tree.

## Tuning in this project
RandomizedSearchCV searches n_estimators, max_depth, min_samples_leaf and max_features. Search folds are chronological month-based folds within training data only.

## Evaluation
CV RMSE is used for model selection; holdout MAE, MSE, RMSE and R² are reported separately. Tree feature importances are saved only if the selected model exposes them.

## Strengths and limitations
Captures nonlinearities and interactions with relatively robust performance. It is less interpretable than linear regression and can be computationally heavier. Feature importance is not causal.

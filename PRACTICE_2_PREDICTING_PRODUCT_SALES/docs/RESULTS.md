# Lab 2 — Experimental Results

## 1. Dataset Overview

Dataset: UCI Online Retail (ID: 352)

- Original records: 541,909
- Original columns: 8
- Target variable: Monthly gross revenue (GBP)
- Aggregation: StockCode by month
- Panel records after preprocessing and feature engineering: 33,167

Revenue is calculated as:

Revenue = Quantity * UnitPrice

Cancelled invoices, missing required values, non-positive quantities,
and non-positive unit prices are excluded.

Each product's monthly panel starts from its first recorded appearance.
Missing months between the first appearance and the final dataset month
are filled with zero revenue.

## 2. Train-Test Split and Model Selection

The dataset was split chronologically without shuffling.

| Set | Records |
|---|---:|
| Training | 25,794 |
| Testing | 7,373 |
| Total panel records | 33,167 |

- Training period: March 2011 – October 2011
- Test period starts: November 2011

Model selection and hyperparameter tuning were performed using
TimeSeriesSplit cross-validation on the training set.

Cross-validation was grouped by complete months to prevent products
from the same month appearing in both training and validation folds.

The final model was selected using the lowest mean CV RMSE.
The independent test set was used for final performance reporting,
not for model selection or hyperparameter tuning.

## 3. Cross-Validation Results

Models are ranked by CV RMSE in ascending order.

| Model | CV RMSE |
|---|---:|
| Random Forest (tuned) | 413.78 |
| Random Forest | 436.36 |
| Gradient Boosting | 484.71 |
| Linear Regression | 502.71 |
| Decision Tree | 503.73 |

Random Forest (tuned) achieved the lowest CV RMSE (413.78 GBP)
and was therefore selected as the final model.

The selected hyperparameters were:

- n_estimators: 200
- max_depth: 12
- min_samples_leaf: 4
- max_features: 0.8

## 4. Independent Test Performance

The following metrics were calculated on the chronological holdout test set.

| Model | MAE (GBP) | MSE | RMSE (GBP) | R² |
|---|---:|---:|---:|---:|
| Gradient Boosting | 218.08 | 578,850.50 | 760.82 | 0.4652 |
| Random Forest | 195.97 | 581,334.66 | 762.45 | 0.4629 |
| Random Forest (tuned) | 221.35 | 602,729.37 | 776.36 | 0.4432 |
| Linear Regression | 212.55 | 644,330.55 | 802.70 | 0.4048 |
| Decision Tree | 219.59 | 680,713.20 | 825.05 | 0.3711 |

Gradient Boosting achieved the lowest test RMSE (760.82 GBP)
and the highest test R² (0.4652).

Random Forest achieved the lowest test MAE (195.97 GBP).

These test results are reported for comparison only.
They do not change the model selected by cross-validation.

## 5. Final Model and Discussion

The final selected model is **Random Forest (tuned)** because it
achieved the lowest CV RMSE on the training data.

Its independent test performance was:

- MAE: 221.35 GBP
- MSE: 602,729.37
- RMSE: 776.36 GBP
- R²: 0.4432

The tuned model did not achieve the best test metrics.
Gradient Boosting performed slightly better on test RMSE and R²,
while the default Random Forest achieved a lower test MAE.

The difference between cross-validation and test performance may
indicate that later months have a different sales distribution from
the earlier training period. This is an important limitation when
forecasting time-dependent retail data.

The model-selection procedure prioritizes CV performance and keeps
the test set independent from model selection.

## 6. Prediction Example

The saved model was tested through `scripts/predict.py` using:

- Product code: 85123A
- lag_1: 100
- lag_2: 120
- lag_3: 110
- month: 12

Output:

Random Forest (tuned) — predicted revenue: 140.82 GBP

This is an illustrative input example used to verify the prediction
script. It is not a verified actual revenue value.

## 7. Generated Artifacts

- `outputs/metrics.json`
- `outputs/model_comparison.csv`
- `outputs/test_predictions.csv`
- `outputs/feature_importance.csv`
- `outputs/figures/actual_vs_predicted.png`
- `outputs/figures/feature_importance.png`
- `outputs/figures/model_comparison.png`
- `outputs/figures/residuals.png`
- `models/best_model.joblib`

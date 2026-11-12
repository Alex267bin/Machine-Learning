# Project Design — Product Sales Forecasting

## WHAT
A reproducible Python pipeline that converts transaction-level retail data into product-month revenue forecasts and compares four regression families plus a tuned Random Forest.

## WHY
Product-level monthly revenue is a measurable proxy for sales activity in the available dataset. A chronological evaluation better represents forecasting than a random split. The project deliberately limits claims to fields actually present in UCI Online Retail.

## HOW — pipeline
```text
UCI Online Retail / local Excel
          |
          v
Validation + cleaning
          |
          v
Product-month revenue aggregation
          |
          v
Monthly panel + lag/rolling features
          |
          v
Chronological train / holdout split
          |
          v
Preprocessing + temporal CV
          |
          +--> Linear Regression
          +--> Decision Tree
          +--> Random Forest
          +--> Gradient Boosting
          +--> Tuned Random Forest
          |
          v
Select by training CV RMSE
          |
          v
Holdout evaluation + diagnostics
          |
          v
metrics.json / CSV / figures / best_model.joblib
```

## Design decisions
- **Panel grain:** one row per StockCode-month; prevents conflating products into one store total.
- **Target:** sum of Quantity × UnitPrice (GBP); cancellations and non-positive transactions are excluded.
- **Missing product-months:** zero revenue after the product's first observed month, not before it first appears.
- **Temporal features:** 1-, 2-, 3-month lags and a three-month rolling mean shifted by one month.
- **Categorical feature:** OneHotEncoder for StockCode with unknown categories ignored.
- **Numeric preprocessing:** median imputation in a ColumnTransformer pipeline.
- **Validation:** TimeSeriesSplit indices are constructed on unique training months so products from the same month stay in the same fold.
- **Selection:** lowest mean CV RMSE on training data. Holdout is not used for selection.
- **Reproducibility:** fixed random seed and saved pipeline artifact.

## Main modules
- `scripts/train.py`: complete data-to-model training and reporting pipeline.
- `scripts/predict.py`: command-line prediction interface.
- `notebooks/02_sales_forecasting.ipynb`: guided notebook.
- `outputs/`: generated metrics, predictions and figures.
- `models/`: serialized model.
- `logs/`: runtime log.

## Risks and interpretation
A temporal holdout can differ substantially from CV folds when sales patterns shift. Report CV and holdout scores separately. Product code one-hot encoding does not provide product semantics. Feature importance from tree models is model-specific and should not be interpreted causally.

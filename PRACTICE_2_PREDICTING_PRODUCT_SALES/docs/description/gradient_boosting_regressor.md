# Gradient Boosting Regressor

## Purpose
A boosted-tree regression candidate for monthly product revenue.

## Input / Output
Uses the shared Lab 2 preprocessing and feature set; returns a continuous predicted revenue in GBP.

## How it works
Trees are added sequentially. Each new tree fits residual/error structure left by the current ensemble, and its contribution is scaled by a learning rate.

## Evaluation
Compared with the same training-only temporal CV RMSE and chronological holdout regression metrics as the other candidates.

## Strengths and limitations
Can model complex nonlinear patterns. Performance depends on hyperparameters and can overfit if trees are too complex or too numerous. The current script uses sklearn defaults except random_state; it does not run a dedicated tuning search for this estimator.

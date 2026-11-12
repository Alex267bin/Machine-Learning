"""Dự báo doanh thu tháng tiếp theo từ các đặc trưng lịch sử."""
import argparse
from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product-code", required=True)
    parser.add_argument("--lag-1", required=True, type=float)
    parser.add_argument("--lag-2", required=True, type=float)
    parser.add_argument("--lag-3", required=True, type=float)
    parser.add_argument("--month", required=True, type=int, choices=range(1, 13))
    args = parser.parse_args()
    artifact_path = ROOT / "models/best_model.joblib"
    if not artifact_path.exists():
        raise FileNotFoundError("Hãy chạy scripts/train.py trước.")
    artifact = joblib.load(artifact_path)
    row = pd.DataFrame([{"StockCode": args.product_code, "lag_1": args.lag_1,
                         "lag_2": args.lag_2, "lag_3": args.lag_3,
                         "rolling_mean_3": (args.lag_1 + args.lag_2 + args.lag_3) / 3,
                         "month_num": args.month}])
    value = max(0.0, float(artifact["pipeline"].predict(row)[0]))
    print(f"{artifact['model_name']} — doanh thu dự báo: {value:,.2f} GBP")


if __name__ == "__main__":
    main()

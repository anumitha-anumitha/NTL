import pandas as pd
from config import COL_CELL, COL_MEAN

# Input from YoY step
df = pd.read_csv("march_22_25_yoy.csv")
df = df.sort_values([COL_CELL, "year"]).reset_index(drop=True)



# Lagged FAST moving average (previous 2 years)
df["fma_2y_lag"] = (
    df.groupby(COL_CELL)[COL_MEAN]
      .shift(1)  # exclude current year
      .rolling(window=2, min_periods=2)
      .mean()
      .reset_index(level=0, drop=True)
)

# Lagged SLOW moving average (previous 3 years)
df["sma_3y_lag"] = (
    df.groupby(COL_CELL)[COL_MEAN]
      .shift(1)  # exclude current year
      .rolling(window=3, min_periods=3)
      .mean()
      .reset_index(level=0, drop=True)
)

# Deviation from lagged slow baseline
df["sma_diff_lag"] = df[COL_MEAN] - df["sma_3y_lag"]

# Lagged MA crossover (momentum vs baseline)
df["ma_crossover_lag"] = df["fma_2y_lag"] > df["sma_3y_lag"]

df.to_csv("march_22_25_ma.csv", index=False)
print("Saved: march_22_25_ma.csv (lagged FMA + lagged SMA)")


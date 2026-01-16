import pandas as pd
from config import COL_CELL, COL_MEAN, EPS

df = pd.read_csv("march_22_25_merged.csv")

df["yoy_1y"] = (
    df.groupby(COL_CELL)[COL_MEAN]
      .pct_change(periods=1)
)

df.to_csv("march_22_25_yoy.csv", index=False)

print("Saved: march_22_25_yoy.csv")

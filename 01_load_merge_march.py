import pandas as pd
from config import FILES, COL_CELL, COL_LAT, COL_LON, COL_MEAN, COL_SUM

dfs = []

for year, path in FILES.items():
    df = pd.read_csv(path)

    df = df[[COL_CELL, COL_LAT, COL_LON, COL_MEAN, COL_SUM]].copy()
    df["year"] = year
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Sort for time-series operations
data = data.sort_values([COL_CELL, "year"]).reset_index(drop=True)

data.to_csv("march_22_25_merged.csv", index=False)

print("Saved: march_22_25_merged.csv")

import pandas as pd
from config import COL_MEAN, YOY_THRESHOLD, SATURATION_Q, EPS

df = pd.read_csv("march_22_25_ma.csv")

# Focus on 2025
df_2025 = df[df["year"] == 2025].copy()

# Make sure we only evaluate cells where lagged baselines exist
# (For 2025, sma_3y_lag uses 2022-2024, so it should exist if data is complete)
df_2025 = df_2025.dropna(subset=["yoy_1y", "fma_2y_lag", "sma_3y_lag", "sma_diff_lag"])

# Saturation cap computed on 2025 values only (best practice)
ntl_cap = df_2025[COL_MEAN].quantile(SATURATION_Q)

# Growth zone (LAGGED logic)
df_2025["growth_zone"] = (
    (df_2025["yoy_1y"] > YOY_THRESHOLD) &
    (df_2025["sma_diff_lag"] > 0) &
    (df_2025["ma_crossover_lag"] == True) &
    (df_2025[COL_MEAN] < ntl_cap)
)

# Growth score (same style as before)
# Score = 0.7 * positive YoY + 0.3 * relative uplift above baseline
df_2025["growth_score"] = (
    0.7 * df_2025["yoy_1y"].clip(lower=0) +
    0.3 * (df_2025["sma_diff_lag"] / (df_2025["sma_3y_lag"] + EPS))
)

# Save outputs (same as before)
df_2025.to_csv("march_2025_growth_analysis.csv", index=False)
df_2025[df_2025["growth_zone"]].to_csv("march_2025_growth_zones_kepler.csv", index=False)

print("Saved:")
print(" - march_2025_growth_analysis.csv")
print(" - march_2025_growth_zones_kepler.csv")

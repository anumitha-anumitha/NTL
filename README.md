# Thailand VIIRS Night-Time Lights – Growth Zone Detection (March-only)

## Overview
This project identifies emerging growth zones in Thailand using VIIRS Night-Time Lights (NTL) data aggregated at a 5 km × 5 km grid level.

The analysis uses March composites only for the years 2022–2025. Growth is detected using:
- Year-on-Year (YoY) growth
- Lagged Fast Moving Average (FMA)
- Lagged Slow Moving Average (SMA)
- Saturation filtering
- Composite growth score

All baselines are lagged (past-only) to avoid self-inclusion bias.

---

## Data Description

### Input files
- Thailand_VIIRS_NightLights_2022-03_5kmGrid_withlatlon.csv
- Thailand_VIIRS_NightLights_2023-03_5kmGrid_withlatlon.csv
- Thailand_VIIRS_NightLights_2024-03_5kmGrid_withlatlon.csv
- Thailand_VIIRS_NightLights_2025-03_5kmGrid_withlatlon.csv

### Columns
- cell_id: Unique grid identifier (5 km × 5 km)
- lat, lon: Grid centroid coordinates
- mean_ntl: Mean night-time light radiance (monthly composite)
- sum_ntl: Total radiance within grid cell

Each value represents an average of all valid nighttime satellite observations during March.

---

## Folder Structure
ntl_march/
├── config.py
├── 01_load_merge_march.py
├── 02_yoy_march.py
├── 03_moving_averages_march.py
├── 04_growth_zone_march.py
└── README.md

---

## Methodology

### Year-on-Year (YoY) Growth
YoY measures year-to-year change for the same grid cell:
YoY_t = (NTL_t − NTL_{t−1}) / NTL_{t−1}

For 2025, this compares March 2025 with March 2024.

---

### Lagged Moving Averages

To avoid dampening and data leakage, current-year values are excluded from baselines.

Fast Moving Average (lagged, 2-year):
FMA_lag(t) = (NTL_{t−1} + NTL_{t−2}) / 2

Slow Moving Average (lagged, 3-year):
SMA_lag(t) = (NTL_{t−1} + NTL_{t−2} + NTL_{t−3}) / 3

SMA Difference:
SMA_diff = NTL_current − SMA_lag

MA Crossover:
MA_crossover = True if FMA_lag > SMA_lag

---

### Saturation Filtering
The top 10% brightest grids (based on 2025 values) are treated as saturated and excluded to focus on emerging regions.

---

### Growth Zone Definition (2025)
A grid cell is classified as a growth zone if:
- YoY growth exceeds threshold
- Current value is above lagged SMA
- Lagged MA crossover is True
- Grid is not saturated

---

### Growth Score
GrowthScore = 0.7 × max(YoY, 0) + 0.3 × (SMA_diff / SMA_lag)

Higher scores indicate stronger and more reliable growth.

---

## Execution Order
python 01_load_merge_march.py
python 02_yoy_march.py
python 03_moving_averages_march.py
python 04_growth_zone_march.py

---

## Outputs
- march_22_25_merged.csv
- march_22_25_yoy.csv
- march_22_25_ma.csv
- march_2025_growth_analysis.csv
- march_2025_growth_zones_kepler.csv

---

## Key Takeaway
YoY captures change, lagged SMA captures baseline, lagged FMA captures momentum, and growth zones represent accelerating, non-saturated expansion areas.

# File paths
FILES = {
    2022: "Thailand_VIIRS_NightLights_2022-03_5kmGrid_withlatlon.csv",
    2023: "Thailand_VIIRS_NightLights_2023-03_5kmGrid_withlatlon.csv",
    2024: "Thailand_VIIRS_NightLights_2024-03_5kmGrid_withlatlon.csv",
    2025: "Thailand_VIIRS_NightLights_2025-03_5kmGrid_withlatlon.csv",
}

# Column names 
COL_CELL = "cell_id"
COL_LAT = "lat"
COL_LON = "lon"
COL_MEAN = "mean_ntl"
COL_SUM  = "sum_ntl"

# Thresholds
YOY_THRESHOLD = 0.15        # 15% YoY growth
SATURATION_Q = 0.90         # top 10% brightness treated as saturated
EPS = 1e-6

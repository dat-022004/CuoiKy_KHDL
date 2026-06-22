"""
Script tạo dataset Đặt xe mẫu thực tế tại Việt Nam
Mô phỏng dữ liệu đặt xe Grab/Be tại TP.HCM
"""
import pandas as pd
import numpy as np
import os

np.random.seed(42)
N = 20000  # số chuyến đi

# --- Thời gian ---
start = pd.Timestamp("2024-01-01")
end   = pd.Timestamp("2024-06-30 23:59:59")
seconds_range = int((end - start).total_seconds())
timestamps = [start + pd.Timedelta(seconds=int(s))
              for s in np.random.randint(0, seconds_range, N)]
timestamps = pd.to_datetime(sorted(timestamps))

# --- Tọa độ (TP.HCM: Q1, Q2, Q3, Q7, Tân Bình) ---
# Phân phối theo khu vực với xác suất thực tế
boroughs = {
    "Quận 1":    {"lat": (10.768, 10.785), "lon": (106.690, 106.708), "prob": 0.40},
    "Quận 3":    {"lat": (10.772, 10.790), "lon": (106.678, 106.692), "prob": 0.20},
    "Tân Bình":  {"lat": (10.795, 10.815), "lon": (106.650, 106.675), "prob": 0.15},
    "Quận 2":    {"lat": (10.780, 10.805), "lon": (106.730, 106.760), "prob": 0.15},
    "Quận 7":    {"lat": (10.720, 10.750), "lon": (106.705, 106.735), "prob": 0.10},
}
borough_names = list(boroughs.keys())
probs = [boroughs[b]["prob"] for b in borough_names]

chosen = np.random.choice(len(borough_names), size=N, p=probs)
lats, lons, areas = [], [], []
for idx in chosen:
    b = borough_names[idx]
    lat = np.random.uniform(*boroughs[b]["lat"])
    lon = np.random.uniform(*boroughs[b]["lon"])
    lats.append(round(lat, 6))
    lons.append(round(lon, 6))
    areas.append(b)

# --- Dịch vụ ---
services = np.random.choice(
    ["GrabBike", "GrabCar", "BeBike", "BeCar", "Gojek"],
    size=N,
    p=[0.45, 0.25, 0.15, 0.10, 0.05]
)

# --- Quãng đường (km) ---
# Phân phối log-normal, trung bình ~5 km
miles = np.round(np.random.lognormal(mean=1.5, sigma=0.6, size=N), 2)
miles = np.clip(miles, 0.5, 30.0)

# --- Thời gian chuyến (phút) ---
# Tương quan với km + kẹt xe (random noise)
trip_minutes = np.round(miles * np.random.uniform(4, 8, N) + np.random.normal(3, 3, N), 1)
trip_minutes = np.clip(trip_minutes, 3, 120)

# --- Tạo DataFrame ---
df = pd.DataFrame({
    "Thoi_gian": timestamps,
    "Vi_do": lats,
    "Kinh_do": lons,
    "Dich_vu": services,
    "Quan_Huyen": areas,
    "Quang_duong_km": miles,
    "Thoi_gian_phut": trip_minutes,
})

# Lưu
os.makedirs("data", exist_ok=True)
df.to_csv("data/doxe_vn_data.csv", index=False)
print(f"[OK] Da tao dataset VN: data/doxe_vn_data.csv")
print(f"   So dong: {len(df):,}")
print(f"   Cot: {list(df.columns)}")
print(df.head())

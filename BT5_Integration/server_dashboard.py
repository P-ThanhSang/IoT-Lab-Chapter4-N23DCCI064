# BT5 Bước 3 — Dashboard phòng server bằng matplotlib
# Nền tảng: QEMU (Raspberry Pi OS)
# Vẽ 3 subplot: Nhiệt độ, Độ ẩm, Khoảng cách + đường ngưỡng

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

# Đọc dữ liệu từ CSV
temps, hums, dists = [], [], []

with open('/home/pi/iot_lab/wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row['temperature']))
        hums.append(float(row['humidity']))
        dists.append(float(row['distance']))

# Vẽ đồ thị 3 subplot
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Subplot 1: Nhiệt độ (đỏ) + ngưỡng 30°C
axes[0].plot(temps, 'r-', linewidth=1.5, label='Nhiet do')
axes[0].axhline(y=30, color='orange', linestyle='--', label='Nguong 30°C')
axes[0].fill_between(range(len(temps)), temps, 30,
                      where=[t > 30 for t in temps],
                      alpha=0.3, color='red')
axes[0].set_ylabel('Temp (°C)')
axes[0].set_title('Server Room Dashboard — Giam sat phong server')
axes[0].legend(loc='upper right')
axes[0].grid(True, alpha=0.3)

# Subplot 2: Độ ẩm (xanh dương) + ngưỡng 80%
axes[1].plot(hums, 'b-', linewidth=1.5, label='Do am')
axes[1].axhline(y=80, color='orange', linestyle='--', label='Nguong 80%')
axes[1].fill_between(range(len(hums)), hums, 80,
                      where=[h > 80 for h in hums],
                      alpha=0.3, color='blue')
axes[1].set_ylabel('Humidity (%)')
axes[1].legend(loc='upper right')
axes[1].grid(True, alpha=0.3)

# Subplot 3: Khoảng cách (xanh lá) + ngưỡng 30cm
axes[2].plot(dists, 'g-', linewidth=1.5, label='Khoang cach')
axes[2].axhline(y=30, color='red', linestyle='--', label='Nguong 30cm')
axes[2].fill_between(range(len(dists)), dists, 30,
                      where=[d < 30 for d in dists],
                      alpha=0.3, color='red')
axes[2].set_ylabel('Distance (cm)')
axes[2].set_xlabel('Sample')
axes[2].legend(loc='upper right')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/pi/iot_lab/server_dashboard.png', dpi=150)
print('Saved: server_dashboard.png')

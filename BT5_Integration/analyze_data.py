# BT5 Bước 2 — Phân tích dữ liệu phòng server
# Nền tảng: QEMU (Raspberry Pi OS)
# Đọc file wokwi_data.csv và tạo báo cáo thống kê

import csv

temps, hums, dists = [], [], []
warnings = 0
criticals = 0
intrusions = 0  # distance < 30cm

with open('/home/pi/iot_lab/wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = float(row['temperature'])
        h = float(row['humidity'])
        d = float(row['distance'])
        temps.append(t)
        hums.append(h)
        dists.append(d)
        if row['status'] == 'WARNING':
            warnings += 1
        if row['status'] == 'CRITICAL':
            criticals += 1
        if d < 30:
            intrusions += 1

total = len(temps)

print('=== BÁO CÁO PHÒNG SERVER ===')
print(f'Tổng mẫu: {total}')
print(f'Nhiệt độ: TB={sum(temps)/total:.1f}°C, Min={min(temps):.1f}, Max={max(temps):.1f}')
print(f'Độ ẩm:    TB={sum(hums)/total:.1f}%, Min={min(hums):.1f}, Max={max(hums):.1f}')
print(f'Khoảng cách: TB={sum(dists)/total:.1f}cm, Min={min(dists):.1f}, Max={max(dists):.1f}')
print(f'Phát hiện người vào: {intrusions} lần (distance < 30cm)')
print(f'Cảnh báo WARNING: {warnings}/{total} ({warnings/total*100:.0f}%)')
print(f'Cảnh báo CRITICAL: {criticals}/{total} ({criticals/total*100:.0f}%)')

# Ghi report
with open('/home/pi/iot_lab/report.txt', 'w') as f:
    f.write('=== BAO CAO PHONG SERVER ===\n')
    f.write(f'Tong mau: {total}\n')
    f.write(f'Nhiet do TB: {sum(temps)/total:.1f}\n')
    f.write(f'Nhiet do Min: {min(temps):.1f}, Max: {max(temps):.1f}\n')
    f.write(f'Do am TB: {sum(hums)/total:.1f}\n')
    f.write(f'Khoang cach TB: {sum(dists)/total:.1f}\n')
    f.write(f'Phat hien nguoi: {intrusions}\n')
    f.write(f'Canh bao WARNING: {warnings}\n')
    f.write(f'Canh bao CRITICAL: {criticals}\n')

print('\nĐã ghi report.txt')

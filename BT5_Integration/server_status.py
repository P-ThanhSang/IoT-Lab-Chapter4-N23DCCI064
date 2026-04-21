# BT5 Bước 4 — Hiển thị trạng thái phòng server trên Sense HAT
# Nền tảng: Sense HAT Emulator (QEMU + SSH X11)
# Tích hợp: bar chart + alert HOT! + joystick hiện nhiệt độ

from sense_emu import SenseHat
import csv
import time

sense = SenseHat()
sense.clear()

# Đọc dòng cuối CSV để lấy giá trị mặc định
try:
    with open('/home/pi/iot_lab/wokwi_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        last = rows[-1]
        default_temp = float(last['temperature'])
        default_hum = float(last['humidity'])
    print(f'Doc CSV: Temp={default_temp}, Hum={default_hum}')
except:
    default_temp = 25.0
    default_hum = 50.0
    print('Khong doc duoc CSV, dung gia tri mac dinh')

# === HÀM MAP GIÁ TRỊ → SỐ CỘT LED ===
def map_value(val, in_min, in_max, out_max=8):
    result = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, result))

# === HÀM VẼ BAR CHART ===
def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0, 0, 0])

# === HÀM VẼ DASHBOARD ===
def draw_dashboard(temp, hum):
    # Bar chart nhiệt độ: hàng 0-2 (đỏ)
    temp_cols = map_value(temp, 15, 50)
    draw_bar(0, 2, temp_cols, [255, 0, 0])

    # Bar chart độ ẩm: hàng 3-5 (xanh dương)
    hum_cols = map_value(hum, 20, 100)
    draw_bar(3, 5, hum_cols, [0, 0, 255])

    # Trạng thái hàng 6-7
    if temp > 35 and hum > 80:
        status_color = [255, 0, 0]      # ĐỎ — nguy hiểm
        status_text = 'NGUY HIEM'
    elif temp > 30 or hum > 80:
        status_color = [255, 255, 0]    # VÀNG — cảnh báo
        status_text = 'CANH BAO'
    else:
        status_color = [0, 255, 0]      # XANH — bình thường
        status_text = 'BINH THUONG'
    draw_bar(6, 7, 8, status_color)

    print(f'Temp: {temp:.1f}C ({temp_cols} cols) | Hum: {hum:.1f}% ({hum_cols} cols) | {status_text}')

    # Nếu temp > 30: hiện cảnh báo HOT!
    if temp > 30:
        sense.show_message('HOT!', text_colour=[255, 0, 0], scroll_speed=0.06)
        draw_dashboard_silent(temp, hum)  # Vẽ lại sau khi text chạy xong

# === VẼ LẠI KHÔNG CÓ ALERT (tránh vòng lặp) ===
def draw_dashboard_silent(temp, hum):
    temp_cols = map_value(temp, 15, 50)
    draw_bar(0, 2, temp_cols, [255, 0, 0])
    hum_cols = map_value(hum, 20, 100)
    draw_bar(3, 5, hum_cols, [0, 0, 255])
    if temp > 35 and hum > 80:
        draw_bar(6, 7, 8, [255, 0, 0])
    elif temp > 30 or hum > 80:
        draw_bar(6, 7, 8, [255, 255, 0])
    else:
        draw_bar(6, 7, 8, [0, 255, 0])

# === VÒNG LẶP CHÍNH ===
print('=== SERVER STATUS DASHBOARD ===')
print('Keo slider de thay doi nhiet do/do am')
print('Bam joystick MIDDLE de hien nhiet do tren LED')
print('Ctrl+C de thoat')
print()

first_run = True
try:
    while True:
        # Đọc cảm biến từ Sense HAT Emulator (slider)
        temp = sense.get_temperature()
        hum = sense.get_humidity()

        # Lần đầu: hiện dashboard
        if first_run:
            draw_dashboard(temp, hum)
            first_run = False
            last_temp = temp
            last_hum = hum

        # Cập nhật khi giá trị thay đổi đáng kể
        if abs(temp - last_temp) > 1 or abs(hum - last_hum) > 1:
            draw_dashboard(temp, hum)
            last_temp = temp
            last_hum = hum

        # Joystick middle: hiện giá trị nhiệt độ text
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                sense.show_message(f'{temp:.0f}C', text_colour=[255, 255, 0], scroll_speed=0.06)
                draw_dashboard_silent(temp, hum)

        time.sleep(0.1)
except KeyboardInterrupt:
    sense.clear()
    print('\nThoat server status.')

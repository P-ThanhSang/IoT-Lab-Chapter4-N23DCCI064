# DHT22 + LED cảnh báo — MicroPython (Wokwi — Raspberry Pi Pico)
# Tác giả: Phạm Thanh Sang — N23DCCI064
# Mô tả: Đọc nhiệt độ/độ ẩm từ DHT22, bật LED cảnh báo theo ngưỡng

from machine import Pin
import dht
import time

# Khởi tạo cảm biến DHT22 và 3 LED
sensor = dht.DHT22(Pin(16))
led_do = Pin(15, Pin.OUT)
led_vang = Pin(14, Pin.OUT)
led_xanh = Pin(13, Pin.OUT)

def tat_het():
    """Tắt tất cả đèn LED"""
    led_do.value(0)
    led_vang.value(0)
    led_xanh.value(0)

print("=== ĐỌC CẢM BIẾN DHT22 + CẢNH BÁO LED ===")

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Nhiệt độ: {temp}°C | Độ ẩm: {hum}%")

        tat_het()
        if temp > 30:
            led_do.value(1)
            print("⚠️ CẢNH BÁO: NHIỆT ĐỘ CAO!")
        elif hum > 80:
            led_vang.value(1)
            print("⚠️ CẢNH BÁO: ĐỘ ẨM CAO!")
        else:
            led_xanh.value(1)
            print("✅ Bình thường.")
    except Exception as e:
        print(f"Lỗi đọc cảm biến: {e}")

    time.sleep(2)

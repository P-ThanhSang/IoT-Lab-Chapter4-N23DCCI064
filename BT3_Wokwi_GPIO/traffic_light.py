# Đèn giao thông — MicroPython (Wokwi — Raspberry Pi Pico)
# Tác giả: Phạm Thanh Sang — N23DCCI064
# Mô tả: Điều khiển 3 LED mô phỏng đèn giao thông Đỏ→Xanh→Vàng

from machine import Pin
import time

# Khởi tạo 3 LED: Đỏ (GP15), Vàng (GP14), Xanh (GP13)
led_do = Pin(15, Pin.OUT)
led_vang = Pin(14, Pin.OUT)
led_xanh = Pin(13, Pin.OUT)

def tat_het():
    """Tắt tất cả đèn LED"""
    led_do.value(0)
    led_vang.value(0)
    led_xanh.value(0)

print("=== ĐÈN GIAO THÔNG ===")
print("Đỏ: 5s → Xanh: 5s → Vàng: 2s")

while True:
    # Đèn ĐỎ — Dừng (5 giây)
    tat_het()
    led_do.value(1)
    print("🔴 ĐỎ — Dừng!")
    time.sleep(5)

    # Đèn XANH — Đi (5 giây)
    tat_het()
    led_xanh.value(1)
    print("🟢 XANH — Đi!")
    time.sleep(5)

    # Đèn VÀNG — Chuẩn bị dừng (2 giây)
    tat_het()
    led_vang.value(1)
    print("🟡 VÀNG — Chuẩn bị dừng!")
    time.sleep(2)

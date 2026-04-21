# Potentiometer + LED 3 mức — MicroPython (Wokwi — Raspberry Pi Pico)
# Tác giả: Phạm Thanh Sang — N23DCCI064
# Mô tả: Đọc ADC từ biến trở, bật LED theo 3 mức THẤP/TB/CAO

from machine import Pin, ADC
import time

# Khởi tạo ADC (GP26) và 3 LED
pot = ADC(Pin(26))
led_do = Pin(15, Pin.OUT)
led_vang = Pin(14, Pin.OUT)
led_xanh = Pin(13, Pin.OUT)

print("=== POTENTIOMETER + LED 3 MỨC ===")

while True:
    raw = pot.read_u16()
    pct = raw / 65535 * 100

    # Tắt hết LED trước
    led_do.value(0)
    led_vang.value(0)
    led_xanh.value(0)

    if pct < 33:
        led_xanh.value(1)
        muc = "THẤP"
    elif pct < 66:
        led_xanh.value(1)
        led_vang.value(1)
        muc = "TRUNG BÌNH"
    else:
        led_xanh.value(1)
        led_vang.value(1)
        led_do.value(1)
        muc = "CAO"

    print(f"ADC: {raw} ({pct:.1f}%) — Mức: {muc}")
    time.sleep(1)

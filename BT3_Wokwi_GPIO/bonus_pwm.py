# PWM điều khiển độ sáng LED — MicroPython (Wokwi — Raspberry Pi Pico)
# Tác giả: Phạm Thanh Sang — N23DCCI064
# Mô tả: Dùng PWM điều khiển độ sáng LED đỏ theo giá trị biến trở

from machine import Pin, ADC, PWM
import time

# Khởi tạo ADC và PWM
pot = ADC(Pin(26))
led_pwm = PWM(Pin(15), freq=1000)

print("=== PWM ĐIỀU KHIỂN ĐỘ SÁNG LED ===")

while True:
    raw = pot.read_u16()
    led_pwm.duty_u16(raw)
    pct = raw / 65535 * 100
    print(f"ADC: {raw} — PWM: {raw} — Độ sáng: {pct:.1f}%")
    time.sleep(0.5)

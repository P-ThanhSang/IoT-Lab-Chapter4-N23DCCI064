# BT3 — GPIO + Cảm biến (Wokwi MicroPython)

**Sinh viên:** Phạm Thanh Sang — N23DCCI064

## Danh sách project Wokwi

| Project | Mô tả | Link |
|---|---|---|
| Đèn giao thông | LED Đỏ→Xanh→Vàng (5s-5s-2s) | [Wokwi Share](https://wokwi.com/projects/461834978837743617) |
| DHT22 + LED | Cảnh báo nhiệt độ/độ ẩm | [Wokwi Share](https://wokwi.com/projects/461834978837743617) |
| Potentiometer | ADC + 3 mức LED | [Wokwi Share](https://wokwi.com/projects/461834978837743617) |
| Bonus PWM | Điều khiển độ sáng LED | [Wokwi Share](https://wokwi.com/projects/461834978837743617) |

## Sơ đồ nối chân
- LED: GP15 (đỏ), GP14 (vàng), GP13 (xanh) → R 220Ω → GND
- DHT22: VCC→3V3, GND→GND, DATA→GP16
- Potentiometer: VCC→3V3, GND→GND, WIPER→GP26 (ADC0)

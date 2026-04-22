# IoT Lab — Chapter 4: Raspberry Pi with Python

**Ho ten:** Pham Thanh Sang
**MSSV:** N23DCCI064
**GitHub:** [P-ThanhSang](https://github.com/P-ThanhSang)

## Danh sach bai tap

| BT | Ten | Nen tang | Thu muc | Trang thai |
|---|---|---|---|---|
| 1 | Giam sat tai nguyen he thong | QEMU | BT1_QEMU_SystemMonitor/ | ✅ Hoan thanh |
| 2 | Mo phong cam bien + do thi | QEMU | BT2_QEMU_SensorSim/ | ✅ Hoan thanh |
| 3 | GPIO + cam bien (MicroPython) | Wokwi | BT3_Wokwi_GPIO/ | ✅ Hoan thanh |
| 4 | Sense HAT Emulator | Sense HAT | BT4_SenseHAT/ | ✅ Hoan thanh |
| 5 | He thong IoT da nen tang | Ca 3 | BT5_Integration/ | ✅ Hoan thanh |
| 6 | Git, GitHub CI/CD | GitHub | .github/workflows/ | ✅ Phan A |
| 7 | Dieu khien LED GPIO Zero | QEMU | BT7_GPIO_Zero/ | ✅ Hoan thanh |
| 8 | File Text trong Python | QEMU | BT8_FileText/ | ✅ Hoan thanh |
| 9 | Truc quan hoa matplotlib | QEMU | BT9_Matplotlib/ | ✅ Hoan thanh |

## Nen tang su dung

- **QEMU**: Raspberry Pi OS Trixie (ARM64) — giam sat he thong, matplotlib, Sense HAT Emulator, GPIO Zero Mock
- **Wokwi**: Raspberry Pi Pico (MicroPython) — GPIO, DHT22, HC-SR04, Potentiometer
- **Sense HAT Emulator**: LED 8x8 matrix, dashboard, joystick mini-game

## Cau truc thu muc

```
IoT-Lab-Chapter4-N23DCCI064/
├── .github/workflows/ci.yml        # GitHub Actions CI
├── BT1_QEMU_SystemMonitor/         # Giam sat CPU/RAM/Disk
│   └── system_monitor.py
├── BT2_QEMU_SensorSim/             # Mo phong cam bien + do thi
│   ├── sensor_sim.py
│   ├── sensor_visualize.py
│   └── sensor_chart.png
├── BT3_Wokwi_GPIO/                 # GPIO + cam bien Wokwi
│   ├── traffic_light.py
│   ├── dht22_led.py
│   ├── pot_led.py
│   └── bonus_pwm.py
├── BT4_SenseHAT/                   # Sense HAT Emulator
│   ├── sensehat_display.py
│   ├── sensehat_icon.py
│   ├── sensehat_sensor.py
│   ├── sensehat_dashboard.py
│   └── sensehat_game.py
├── BT5_Integration/                # He thong IoT tich hop
│   ├── bt5_server_main.py
│   ├── analyze_data.py
│   ├── server_dashboard.py
│   ├── server_status.py
│   ├── wokwi_data.csv
│   └── report.txt
├── BT7_GPIO_Zero/                  # Dieu khien LED (Mock Mode)
│   ├── led1.py
│   ├── led2.py
│   ├── led3.py
│   └── led4.py
├── BT8_FileText/                   # Thao tac file text
│   ├── make_txtfile.py
│   ├── write_txtfile.py
│   ├── append_txtfile.py
│   └── read_txtfile.py
├── BT9_Matplotlib/                 # Truc quan hoa du lieu
│   ├── plt_1.py
│   ├── plt_2.py
│   ├── plt_3.py
│   └── temp_sim_visualization.py
├── screenshots/                    # Anh minh chung BT0-BT9
└── README.md
```

## CI/CD

- **GitHub Actions**: Lint (flake8) + Test + Structure check
- Pipeline status: ✅ Green

from gpiozero import LED
from time import sleep


# Dictionary quan ly 3 LED (theo Slide Bai 1.1)
leds = {
    "red": LED(5),
    "yellow": LED(6),
    "green": LED(13),
}


# Nhay tuan tu tung LED
for name, led in leds.items():
    print(f'Nhay LED {name}...')
    led.blink(on_time=1, off_time=1)
    sleep(2)
    led.off()


print('Hoan thanh nhay 3 LED.')

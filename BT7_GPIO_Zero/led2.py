from gpiozero import LED
from signal import pause


led = LED(20)


led.blink(on_time=3, off_time=1)
pause()  # Cho tin hieu — khong can vong lap while

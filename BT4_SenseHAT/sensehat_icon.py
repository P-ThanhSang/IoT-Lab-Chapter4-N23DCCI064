from sense_emu import SenseHat
import time

sense = SenseHat()

# Dinh nghia mau
r = [255, 0, 0]
p = [255, 105, 180]
b = [0, 0, 0]

# Trai tim 8x8 — TU THIET KE
heart = [
    b, r, r, b, b, r, r, b,
    r, p, r, r, r, p, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b,
]

sense.set_pixels(heart)
print('Bieu tuong trai tim da hien thi.')
time.sleep(5)
sense.clear()

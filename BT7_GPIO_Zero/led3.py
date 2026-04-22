from gpiozero import LED


led = LED(20)


while True:
    cmd = input('Nhap lenh (on/off/exit): ').strip().lower()
    if cmd == 'on':
        led.on()
        print('LED da BAT')
    elif cmd == 'off':
        led.off()
        print('LED da TAT')
    elif cmd == 'exit':
        led.off()
        print('Thoat chuong trinh.')
        break
    else:
        print('Lenh khong hop le: ' + cmd)

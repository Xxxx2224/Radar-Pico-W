import machine
import utime


triq=Pin(19,Pin.OUT)
echo=Pin(18,Pin.IN)
triq.value(0)
utime.sleep_us(2)
triq.value(1)
utime.sleep_us(10)
triq.value(0)
while echo.value()==0:
    pass
pulse_start=utime.ticks_us()
while echo.value()==1:
    pass
pulse_stop=utime.ticks_us()
pulse_fark=utime.ticks_diff(pulse_stop,pulse_start)
mesafe=pulse_fark*(0.0346/2)
print('{:.2f}'.format(mesafe))
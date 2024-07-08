from machine import Pin, PWM
import time
import math
servo = PWM(Pin(28))
servo.freq(50)
def motoraci(acI):
    xxx=acI
    min=(1/20)*(2**16-1)
    max=(2/20)*(2**16-1)
    minumum=math.ceil(min)
    maximum=math.floor(max)
    acI=math.floor((1/20)*(2**16-1)*(acI/180)+min)
    acIx=math.floor(((3276.75/180)*xxx)+3276.75)
    print(min)
    print(max)
    print(minumum)
    print(maximum)
    print(type(min))
    print(type(max))
    print(type(maximum))
    print(type(minumum))
    print(acI)
    print(type(acI))
    print(acIx)
    print(type(acIx))
motoraci(90)
while True:
    for a in range(1802,8000,100):
       servo.duty_u16(a)
       time.sleep_ms(8)
    for a in range(8000,1802,-100):
       servo.duty_u16(a)
       time.sleep_ms(8)





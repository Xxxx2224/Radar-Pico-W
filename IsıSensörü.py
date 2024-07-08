import machine
import time
import network
import socket
import math
adc=machine.ADC(4)
conversion = 3.3 / (65535)
class Sıcak:
    @staticmethod
    def Delay(x):
        while True:
            read=adc.read_u16()*conversion
            sıcaklık=27-(read-0.706)/0.001721
            print(sıcaklık)
            time.sleep(x)
    @staticmethod
    def oku():
        while True:
            read=adc.read_u16()*conversion
            sıcaklık=27-(read-0.706)/0.001721
            print(sıcaklık)
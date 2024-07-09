import network
import socket
import _thread
from machine import Pin, PWM, SPI
import utime
import urequests
import math
from ST7735 import TFT
from sysfont import sysfont
machine.freq(190000000)
print('servo motor test ediliyor...')
servo = PWM(Pin(28))
servo.freq(50)
triq=Pin(19,Pin.OUT)
echo=Pin(18,Pin.IN)
led=machine.Pin('LED',machine.Pin.OUT)
adc=machine.ADC(4)
conversion = 3.3 / (65535)
a='Veri Yok'
i=0
mesafe='Veri yok'
sicaklik=0
nesne='Veri Yok'
#Genişlik 1-160 Yükseklik 2-127
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=None)
Pin_DC = 14
Pin_Reset = 13
Pin_CS = 15
tft=TFT(spi,14,13,15)
tft.initr()
tft.rgb(True)
tft.rotation(1)
def draw_circle(tft, x0, y0, radius, color):
    f = 1 - radius
    ddF_x = 1
    ddF_y = -2 * radius
    x = 0
    y = radius

    tft.pixel((x0, y0 + radius), color)
    tft.pixel((x0, y0 - radius), color)
    tft.pixel((x0 + radius, y0), color)
    tft.pixel((x0 - radius, y0), color)

    while x < y:
        if f >= 0:
            y -= 1
            ddF_y += 2
            f += ddF_y
        x += 1
        ddF_x += 2
        f += ddF_x

        tft.pixel((x0 + x, y0 + y), color)
        tft.pixel((x0 - x, y0 + y), color)
        tft.pixel((x0 + x, y0 - y), color)
        tft.pixel((x0 - x, y0 - y), color)
        tft.pixel((x0 + y, y0 + x), color)
        tft.pixel((x0 - y, y0 + x), color)
        tft.pixel((x0 + y, y0 - x), color)
        tft.pixel((x0 - y, y0 - x), color)
def core_1():
    global mesafe
    global i
    global nesne
    while True:
        tft.fill(TFT.BLACK)
        tft.line((0,2),(160,2),TFT.GREEN)
        tft.line((1,0),(1,128),TFT.RED)
        tft.line((160,0),(160,128),TFT.BLUE)
        tft.line((0,127),(160,127),TFT.YELLOW)
        tft.line((0,128),(160,128),TFT.RED)

        #def draw_circle(tft, x0, y0, radius, color):
        draw_circle(tft,80,115,110,TFT.GREEN)
        draw_circle(tft,80,115,85,TFT.GREEN)
        draw_circle(tft,80,115,65,TFT.GREEN)
        draw_circle(tft,80,115,40,TFT.GREEN)
        for a in range(115,127,1):
            tft.line((0,a),(160,a),TFT.BLACK)
        tft.line((0,115),(160,115),TFT.GREEN)
        tft.pixel((80,115),TFT.BLUE)
        draw_circle(tft,80,115,5,TFT.GREEN)
        
        tft.text((70,20),'85CM',TFT.RED,sysfont)
        tft.text((70,40),'65CM',TFT.RED,sysfont)
        tft.text((70,65),'40CM',TFT.RED,sysfont)
        tft.text((100,118),'Derece:',TFT.RED,sysfont)
        tft.text((4,118),'Uzaklik:',TFT.RED,sysfont)
        tft.text((55,118),'10',TFT.RED,sysfont)
        for i in range(3,180,1):
            triq.value(0)
            utime.sleep_us(2)
            triq.value(1)
            utime.sleep_us(10)
            triq.value(0)
            start_time = utime.ticks_us()
            while echo.value() == 0:
                if utime.ticks_diff(utime.ticks_us(), start_time) > 600000: 
                    print("echo pini yüksek olaması beklenirken timeout oluştu...")
                    print(i)
                    break
            pulse_start=utime.ticks_us()
            start_time = utime.ticks_us()
            while echo.value() == 1:
                if utime.ticks_diff(utime.ticks_us(), start_time) > 38000:  
                    print("echo pini düşük olaması beklenirken timeout oluştu...")
                    break
            pulse_stop=utime.ticks_us()
            pulse_fark=utime.ticks_diff(pulse_stop,pulse_start)
            mesafe=pulse_fark*(0.0346/2)
            tft.text((55,118),str('{:.2f}'.format(mesafe)),TFT.RED,sysfont)
            if mesafe>100:
                nesne='Nesne Yok'
                tft.pixel((80+round(113*math.cos(math.radians(i-2))),115-round(113*math.sin(math.radians(i-2)))),TFT.BLUE)
                
            if mesafe<=100:
                nesne='Nesne Var'
                tft.pixel((80+round(mesafe*math.cos(math.radians(i-2))),115-round(mesafe*math.sin(math.radians(i-2)))),TFT.BLUE)
            servo.duty_u16(math.floor(((6000/180)*i)+1802))
            tft.line((80,115),(80+round(110*math.cos(math.radians(i))),115-round(110*math.sin(math.radians(i)))),TFT.RED)
            tft.line((80,115),(80+round(110*math.cos(math.radians(i-1))),115-round(110*math.sin(math.radians(i-1)))),TFT.BLACK)
            tft.pixel((80+round(85*math.cos(math.radians(i-2))),115-round(85*math.sin(math.radians(i-2)))),TFT.GREEN)
            tft.pixel((80+round(65*math.cos(math.radians(i-2))),115-round(65*math.sin(math.radians(i-2)))),TFT.GREEN)
            tft.pixel((80+round(40*math.cos(math.radians(i-2))),115-round(40*math.sin(math.radians(i-2)))),TFT.GREEN)
            tft.text((140,118),str(i),TFT.RED,sysfont)
            if i>=70 or i<=110:
                
                tft.text((70,20),'85CM',TFT.RED,sysfont)
                tft.text((70,40),'65CM',TFT.RED,sysfont)
                tft.text((70,65),'40CM',TFT.RED,sysfont)
            
        tft.fill(TFT.BLACK)
        tft.line((0,2),(160,2),TFT.GREEN)
        tft.line((1,0),(1,128),TFT.RED)
        tft.line((160,0),(160,128),TFT.BLUE)
        tft.line((0,127),(160,127),TFT.YELLOW)
        tft.line((0,128),(160,128),TFT.RED)

        
        draw_circle(tft,80,115,110,TFT.GREEN)
        draw_circle(tft,80,115,85,TFT.GREEN)
        draw_circle(tft,80,115,65,TFT.GREEN)
        draw_circle(tft,80,115,40,TFT.GREEN)
        for a in range(115,127,1):
            tft.line((0,a),(160,a),TFT.BLACK)
        tft.line((0,115),(160,115),TFT.GREEN)
        tft.pixel((80,115),TFT.BLUE)
        draw_circle(tft,80,115,5,TFT.GREEN)
        tft.text((100,118),'Derece:',TFT.RED,sysfont)
        tft.text((70,20),'85CM',TFT.RED,sysfont)
        tft.text((70,40),'65CM',TFT.RED,sysfont)
        tft.text((70,65),'40CM',TFT.RED,sysfont)
        tft.text((4,118),'Uzaklik:',TFT.RED,sysfont)
        for i in range(177,0,-1):
            triq.value(0)
            utime.sleep_us(2)
            triq.value(1)
            utime.sleep_us(10)
            triq.value(0)
            start_time = utime.ticks_us()
            while echo.value() == 0:
                if utime.ticks_diff(utime.ticks_us(), start_time) > 6000: 
                    print("Timeout waiting for echo to go high")
                    print(i)
                    break
            pulse_start=utime.ticks_us()
            start_time = utime.ticks_us()
            while echo.value() == 1:
                if utime.ticks_diff(utime.ticks_us(), start_time) > 38000:  
                    print("Timeout waiting for echo to go low")
                    break
            pulse_stop=utime.ticks_us()
            pulse_fark=utime.ticks_diff(pulse_stop,pulse_start)
            mesafe=pulse_fark*(0.0346/2)
            tft.text((55,118),str('{:.2f}'.format(mesafe)),TFT.RED,sysfont)
            if mesafe>100:
                nesne='Nesne Yok'
                tft.pixel((80+round(113*math.cos(math.radians(i+2))),115-round(113*math.sin(math.radians(i+2)))),TFT.BLUE)
            if mesafe<=100:
                nesne='Nesne Var'
                tft.pixel((80+round(mesafe*math.cos(math.radians(i+2))),115-round(mesafe*math.sin(math.radians(i+2)))),TFT.BLUE)
            servo.duty_u16(math.floor(((6000/180)*i)+1802))
            tft.line((80,115),(80+round(110*math.cos(math.radians(i))),115-round(110*math.sin(math.radians(i)))),TFT.RED)
            tft.line((80,115),(80+round(110*math.cos(math.radians(i+1))),115-round(110*math.sin(math.radians(i+1)))),TFT.BLACK)
            tft.pixel((80+round(85*math.cos(math.radians(i+2))),115-round(85*math.sin(math.radians(i+2)))),TFT.GREEN)
            tft.pixel((80+round(65*math.cos(math.radians(i+2))),115-round(65*math.sin(math.radians(i+2)))),TFT.GREEN)
            tft.pixel((80+round(40*math.cos(math.radians(i+2))),115-round(40*math.sin(math.radians(i+2)))),TFT.GREEN)
            tft.text((140,118),str(i),TFT.RED,sysfont)
            if i==100:
                for i in range(118,127,1):
                    tft.line((140,i),(160,i),TFT.BLACK)
            if i==10:
                for i in range(118,127,1):
                    tft.line((140,i),(160,i),TFT.BLACK)
            if i==50:
                tft.pixel((80+round(50*math.cos(math.radians(i-2))),115-round(50*math.sin(math.radians(i-2)))),TFT.BLUE)
                tft.pixel((80+round(87*math.cos(math.radians(i-2))),115-round(87*math.sin(math.radians(i-2)))),TFT.BLUE)
            if i>=70 or i<=110:
                tft.text((70,20),'85CM',TFT.RED,sysfont)
                tft.text((70,40),'65CM',TFT.RED,sysfont)
                tft.text((70,65),'40CM',TFT.RED,sysfont)


def STAinit(x,y):
        global i
        global sicaklik
        global nesne
        global a
        global nesne
        global mesafe
        STA=network.WLAN(network.STA_IF)
        STA.active(True)
        STA.connect(x,y)
        while STA.isconnected()==False:
            if STA.status()==network.STAT_IDLE:
                print('Bağlantı ve Aktivite yok')
                utime.sleep(1)
            elif STA.status()==network.STAT_CONNECTING:
                print('Bağlantı devam ediyor...')
                utime.sleep(1)
            elif STA.status()==network.STAT_WRONG_PASSWORD:
                print('Parola yanlış Tekrar denemek icin init fonksiyonunu tekrar kullan')
                utime.sleep(1)
            elif STA.status()==network.STAT_NO_AP_FOUND:
                print('Hiçbir erişim noktası yanıt vermediği için başarısız oldu')
                utime.sleep(1)
            elif STA.status()==network.STAT_CONNECT_FAIL:
                print('Diğer sorunlar nedeniyle başarısız oldu')
                utime.sleep(1)
            else:
                print('bağlanılıyor...')
                utime.sleep(1)
        if STA.isconnected()==True:
            print('bağlandı')
        Ağ_statü=STA.ifconfig()
        ip=STA.ifconfig()[0]
        print(ip)
        soket=socket.socket()
        soket.bind((ip,80))
        
        while True:
            utime.sleep(0.08)
            read=adc.read_u16()*conversion
            sicaklik=27-(read-0.706)/0.001721
            url = 'http://192.168.187.130:5000/api/data'
            data = {
                'sicakli':sicaklik,
                'derece':i,
                'nesne':nesne,
                'mesafe':mesafe,
                'led':a,
                'ip':ip
                }
            
            try:
                response = urequests.post(url, json=data)
                print(response.text)
                response_data = response.json()
                response.close()
                if 'led_state' in response_data:
                    led.value(response_data['led_state'])
                    if 0==response_data['led_state']:
                        a='Kapali'
                    else:
                        a='Acik'
                
            except Exception as e:
                print("Failed to send data:", e)
           
_thread.start_new_thread(core_1,())
STAinit('xiaomi','25252525..')








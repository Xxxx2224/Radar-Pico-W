import machine
import utime
import network
import socket
import math
led=machine.Pin('LED',machine.Pin.OUT)
adc=machine.ADC(4)
conversion = 3.3 / (65535)
def STAinit(x,y):
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
                print('muhtemelen döngü sırasında bağlantı kuruldu')
                utime.sleep(1)
        if STA.isconnected()==True:
            print('bağlandı')
            
            utime.sleep(2)
        Ağ_statü=STA.ifconfig()
        ip=STA.ifconfig()[0]
        print(ip)
        soket=socket.socket()
        soket.bind(('0.0.0.0',80))
        soket.listen(1)
        while True:
            read=adc.read_u16()*conversion
            sicaklik=27-(read-0.706)/0.001721
            istemci,İst_ip=soket.accept()
            print('istemci ip adresi=',İst_ip)
            istek=istemci.recv(1024)
            istek=istek.decode("utf-8")
            istekler=istek.split()
            url=istekler[1]
            if url.find("led_on") != -1 :
                a='Led Acik'
                led.value(1)
            elif url.find("led_off") != -1:
                a='Led Kapali'
                led.value(0)
            else:
                pass
            file=open("arayüz.html")
            arayüz=file.read()
            file.close()
            arayüz=arayüz.replace("durum",a)
            arayüz=arayüz.replace("sicaklik1",str(sicaklik))
            istemci.send(arayüz)
            istemci.close()
STAinit('SUPERONLINE_Wi-Fi_4993','Aksaray3434')

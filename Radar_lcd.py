from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
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
    tft.text((4,118),'Uzaklik:10',TFT.RED,sysfont)
    for i in range(3,180,1):
        tft.line((80,115),(80+round(110*math.cos(math.radians(i))),115-round(110*math.sin(math.radians(i)))),TFT.RED)
        tft.line((80,115),(80+round(110*math.cos(math.radians(i-1))),115-round(110*math.sin(math.radians(i-1)))),TFT.BLACK)
        tft.pixel((80+round(85*math.cos(math.radians(i-2))),115-round(85*math.sin(math.radians(i-2)))),TFT.GREEN)
        tft.pixel((80+round(65*math.cos(math.radians(i-2))),115-round(65*math.sin(math.radians(i-2)))),TFT.GREEN)
        tft.pixel((80+round(40*math.cos(math.radians(i-2))),115-round(40*math.sin(math.radians(i-2)))),TFT.GREEN)
        tft.text((140,118),str(i),TFT.RED,sysfont)
        if i==50:
            tft.pixel((80+round(50*math.cos(math.radians(i-2))),115-round(50*math.sin(math.radians(i-2)))),TFT.BLUE)
            tft.pixel((80+round(87*math.cos(math.radians(i-2))),115-round(87*math.sin(math.radians(i-2)))),TFT.BLUE)
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
    tft.text((100,118),'Derece:',TFT.RED,sysfont)
    tft.text((70,20),'85CM',TFT.RED,sysfont)
    tft.text((70,40),'65CM',TFT.RED,sysfont)
    tft.text((70,65),'40CM',TFT.RED,sysfont)
    tft.text((4,118),'Uzaklik:10',TFT.RED,sysfont)
    for i in range(177,0,-1):
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


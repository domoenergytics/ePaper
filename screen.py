# -*- coding: utf-8 -*-

import time
import spidev as SPI
import EPD_driver
import datetime
from PIL import Image

xDot = 200
yDot = 200
im = Image.open("logo.bmp")
print(im.format, im.size, im.mode, im.width)
ar = []
px=im.load()
x=0
X = 7
while (x < im.width):
	y=0
	while (y < im.height):
		i=0
		b=0
		while (i < 8):
			b += 2**(7-i) * px[x,y+i]
			i = i+1
		ar.append(b)
		y = y+8
	x= x+1
	X = X-2
	if (X<-8):
		X = 7

bus = 0 
device = 0
disp = EPD_driver.EPD_driver(spi=SPI.SpiDev(bus, device))

# Initialisation de l'écran
print '------------init and Clear part screen------------'
disp.Dis_Clear_part()

#Show part pic
print '------------Show part pic------------'
disp.Dis_part_pic(0,xDot-1,0,yDot-1,ar)




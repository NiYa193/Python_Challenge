#!/bin/bash/python
#coding=utf-8

import Image  
  
img = Image.open('cave.jpg')  
w = img.size[0]  
h = img.size[1]  
      
odd = even = Image.new(img.mode, (w/2, h/2))  
      
for x in range(w):  
	for y in range(h):
		pixel = img.getpixel((x, y))  
		if x % 2 == 0 and y % 2 == 0:  
                	odd.putpixel((x/2, y/2), pixel)  
		elif x % 2 == 1 and y % 2 == 0:  
                	even.putpixel(((x-1)/2, y/2), pixel)
		elif x % 2 == 0 and y % 2 == 1:
			even.putpixel((x/2, (y-1)/2), pixel)
		elif x % 2 == 1 and y % 2 == 1:
			odd.putpixel(((x-1)/2, (y-1)/2), pixel)
odd.show()  
even.show()

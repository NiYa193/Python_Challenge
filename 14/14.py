#!/bin/bash/python
#coding=utf-8

import Image  
  
f = Image.open("wire.png")  
newf = Image.new(f.mode,(100,100))

doubled_steps=200
directions=[(1,0), (0,1), (-1,0), (0,-1)]
x,y,p=-1,0,0 
while doubled_steps//2 > 0:  
	for v in directions:  
		steps=doubled_steps//2 
		for s in range(steps):  
			x,y=x+v[0],y+v[1]  
			print x, y  
			newf.putpixel((x,y),f.getpixel((p,0)))  
			p+=1
		doubled_steps-=1  
newf.show()  

#!/bin/bash/python
#coding=utf-8

info=open('evil2.gfx').readline()  
for i in range(5):  
	f = open("12_f%d.jpg" %i, "wb")
	f.write(info[i::5])
	f.close()  

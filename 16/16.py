#!/bin/bash/python
#coding=utf-8
import Image

old = Image.open('mozart.gif')
s = old.size
data = list(old.getdata())
new = Image.new(old.mode,s)
new.putpalette(old.palette)

receive = new.load()
for i in range(s[1]):
    for j in range(s[0]):
        if data[i*s[0]+j] == 195:
            for pix,x in zip(data[i*s[0]+j:s[0]*(i+1)]+data[i*s[0]:i*s[0]+j-1],range(s[0])):
                receive[x,i]=pix
            break

new.save('new.gif',old.format)

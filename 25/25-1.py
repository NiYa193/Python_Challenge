#!/bin/bash/python
#coding=utf-8

import wave,Image  
new = []  
for i in range(1,26):  
    f = wave.open('lake%d.wav' % i, 'rb')  
    new.append(Image.fromstring('RGB', (60,60), (f.readframes(f.getnframes()))))  

img = Image.new('RGB',(300,300))  
for i in range(25):  
    img.paste(new[i],((i%5)*60, (i/5)*60))  
img.save('lake.png')  

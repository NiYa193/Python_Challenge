#!/usr/bin/python
#coding=utf-8


import Image

file = Image.open('oxygen.png')

print ('').join([chr(file.getpixel((i,43))[0]) for i in xrange(0,609,7)])

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]  
print(''.join(chr(x) for x in result))  

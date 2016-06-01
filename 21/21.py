#!/bin/bash/python
#coding=utf-8

import zlib, bz2  
  
h = open("package.pack")
data = h.read()  
h.close()  
  
output = []  
  
while True:  
    if data.startswith("BZh"):  
        data = bz2.decompress(data)  
        output.append("#")  
    elif data.startswith("x\x9c"):  
        data = zlib.decompress(data)  
        output.append(" ")  
    elif data.endswith("\x9cx"):  
        data = data[::-1]  
        output.append("\n")  
    else:  
        break  
  
print "".join(output)

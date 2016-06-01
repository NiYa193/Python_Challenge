#!/bin/bash/python
#coding=utf-8
import urllib,bz2  

f = urllib.urlopen('http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html')  
s= [chr(len(i)-1) for i in f.readlines()[12::]]  
text = ''.join(s)  
print bz2.decompress(text)

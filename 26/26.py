#!/bin/bash/python
#coding=utf-8
import md5  

f = open('mybroken.zip','rb').read()  
for i in range(len(f)):  
	for j in range(256):  
		newtext = f[:i]+chr(j)+f[i+1:]  
		if md5.md5(newtext).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':  
			open('mybroken_new.zip','wb').write(newtext)  

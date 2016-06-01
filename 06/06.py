#!/bin/bash/python
#coding=utf-8

import re
import zipfile

file = zipfile.ZipFile('channel.zip')
filelst =  file.namelist()
id = '90052'
i=1
result = ""
while (i<3000):
	filenm = id+'.txt'
	print filenm
	f= file.getinfo(filenm)
	line =file.read(filenm)
	m=re.search("is (\d+)",line)
	if m:
		id = m.group(1)
	else:
		print line
		i=3000	
	i+=1
	result+=f.comment

print result

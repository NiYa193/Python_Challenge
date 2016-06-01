#!/usr/bin/python
#coding=utf-8

import urllib2

content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
format = 'abcdefghijklmnopqrstuvwxyz0123456789 .'
for c in content:
	if not c in format:
		content = content.replace(c,"")
ind = content.index("below")+5
print (content[ind:]+".html")

#!/usr/bin/python
#coding=utf-8

import urllib2
import re

content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
m = re.findall("[a-z0-9]+[A-Z]{3}([a-z])[A-Z]{3}[a-z0-9]+",content)
for e in m:
	print e,

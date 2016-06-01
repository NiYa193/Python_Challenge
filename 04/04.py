#!/usr/bin/python
#coding=utf-8

import requests
import re

i=1
id='6523'

while (i<400):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+id
	print url
	content=requests.get(url).content
	m = re.search('is (\d+)',content)
	if m:
		id= m.group(1)
	else:
		print  content
		i=400
	i+=1

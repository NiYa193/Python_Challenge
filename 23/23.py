#!/bin/bash/python
#coding=utf-8

import string
  
dd = "abcdefghijklmnopqrstuvwxyz"  
for i in range(26):
	print i,string.translate("va gur snpr bs jung",string.maketrans(dd,dd[i::]+dd[0:i:]))  

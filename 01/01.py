#!/usr/bin/python
#coding=utf-8
import string

enc="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url='map'
for e in range(0,len(enc)):
	if ord(enc[e])<=ord("x") and ord(enc[e])>=ord("a"):
		print (chr(ord(enc[e])+2),)
	elif ord(enc[e])>ord("x"):
		print (chr(ord(enc[e])-24),)
	else:
		print (enc[e],)
print ("\n---------------------------")
table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print(enc.translate(table))
print(url.translate(table))

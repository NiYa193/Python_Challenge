#!/bin/bash/python
#coding=utf-8

import pickle
import sys

obj = pickle.load(open("banner.p","r"))

for i in obj:
	for n in i:
		print n[0]*n[1]+'\b',
	print
print

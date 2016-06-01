#!/bin/bash/python
#coding=utf-8

from calendar import isleap  
from datetime import date  

TUESDAY = 1  

for year in range(1006, 2000, 10):  
	t = date(year, 1, 27)  
	if isleap(year) and t.weekday() == TUESDAY:  
		print t.isoformat()  

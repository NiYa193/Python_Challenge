#!/bin/bash/python
#coding=utf-8

import urllib  
for count in range(1,26):  
    url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%d.wav" % count  
    urllib.urlretrieve(url, 'lake%d.wav' % count)  

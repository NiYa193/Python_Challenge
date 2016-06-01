#!/bin/bash/python
#coding=utf-8

import base64
  
text = open('att.txt','r').read()  
indian = open('indian.wav','wb')  
wav = base64.b64decode(text)  
indian.write(wav)  
indian.close()  

#!/bin/bash/python
#coding=utf-8

import Image,math
img = Image.open('beer2.png')
f = img.getdata()
color = img.getcolors()
for i in range(65,-1,-2):
    s = []
    t = []
    for j in f:
        if j!=color[i][1] and j!=color[i-1][1]:
            s.append(j)
            t.append(0)
        else:
            if j==color[i][1]:
                t.append(1)
            else:
                t.append(0)
    f = s
    n = int(math.sqrt(len(t)))
    new = Image.new('1',(n,n))
    new.putdata(t)
    new.save('33\%d.png' % ((i-1)/2))

#Final Answer:gremlins

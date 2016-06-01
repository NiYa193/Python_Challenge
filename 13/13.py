#!/bin/bash/python
#coding=utf-8

import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')  
print server.system.listMethods()

print server.phone('Bert')

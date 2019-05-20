#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys

print sys.path

print(u"你好");

a = True
if a :
	print 'a is true'
else :
  print 'a is false'



def aa() :
	a = 1 + 1;
	return a;

print aa.__name__

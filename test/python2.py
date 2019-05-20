#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

'''
文件操作
'''

# 读取文件
try:
  f = open('d:\\aa.txt','r')
  print f.read()
except IOError as e:
  print 'No such file'
finally:
  if 'f' in dir():
    f.close()

# 写文件
try:
  f1 = open('d:\\aa1.txt','w')
  f1.write('Hello')
except IOError as e:
  print 'No such file %s' % e
finally:
  if 'f1' in dir():
    f1.close()
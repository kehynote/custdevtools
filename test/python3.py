#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
数据库操作
'''

import psycopg2

try:
  conn = psycopg2.connect(database="test", user="test", password="test", host="127.0.0.1", port="5432")

  cur = conn.cursor()

  cur.execute("insert into t_test (id,name,age,address,salary) values (1,'test1',20,'wuhan',10000.00)")

  conn.commit()
except Exception as e:
  print 'psycopg2 error: %s' % e
finally:
  if conn:
    conn.close();
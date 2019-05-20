#!/usr/bin/python
#-*- coding:utf-8 -*-

import psycopg2


class TestDB(object):
    """数据库操作类"""

    def __init__(self):
        super(TestDB, self).__init__()

    def listTest(self):
        '''
        列出表t_test数据
        '''
        try:
            conn = psycopg2.connect(
                database="test", user="test", password="test", host="127.0.0.1", port="5432")

            cur = conn.cursor()

            cur.execute('''
        SELECT
          T . ID,
          T ."name",
          T .age,
          T .address
        FROM
          t_test T
        ''')

            rows = cur.fetchall()
        except Exception as e:
            print 'psycopg2 error: %s' % e
        finally:
            if conn:
                conn.close()
        if rows:
            return rows
        else:
            return []

#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
urllib 模块
'''

import urllib2;

class UrllibHelper(object):
    """urllib 帮助类"""

    def __init__(self):
        super(UrllibHelper, self).__init__()

    def openurl(self, url):
        response = urllib2.urlopen(url)
        print response.read().decode('utf-8')

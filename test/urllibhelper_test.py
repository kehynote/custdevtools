#!/usr/bin/python
#-*- coding:utf-8 -*-

import unittest
from kehydb.urllibhelper import UrllibHelper


class UrllibHelperTest(unittest.TestCase):
    """urllibhelper 测试"""

    def test_openurl(self):
        helper = UrllibHelper();
        helper.openurl("http://www.baidu.com")
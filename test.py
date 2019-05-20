#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
单元测试的入口
'''

import unittest

from test.urllibhelper_test import UrllibHelperTest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UrllibHelperTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
# -*- coding: utf-8 -*-
import threading
import time

class test(object):
    s = 1

    def __init__(self):
        self.t = 2
        pass

    @classmethod
    def testFunc1(cls):
        print(cls.s)
        pass

    @staticmethod
    def testFunc2():
        pass
    pass


test1 = test()
test1.testFunc1()
test.testFunc2()
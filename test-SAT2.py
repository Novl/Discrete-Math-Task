# -*- coding: UTF-8 -*-
import SAT2
import unittest

class TestSAT2(unittest.TestCase):
    def setUp(self):
        pass

    def testforsimple(self):
        t = SAT2.main("simple.txt")
        self.assertTrue(t == 1)

    def test1(self):
        t = SAT2.main("test1")
        self.assertTrue(t == 1)

    def test2(self):
        t = SAT2.main("test2")
        self.assertTrue(t == 1)

    def test3(self):
        t = SAT2.main("test3")
        self.assertTrue(t == 0)

    def testABRA(self):
        t = SAT2.main("testABRA")
        self.assertTrue(t != 1 and t != 0)

    def test4(self):
        t = SAT2.main("test4")
        self.assertTrue(t == 1)

    def test5(self):
        t = SAT2.main("test5")
        self.assertTrue(t == 0)

if __name__ == '__main__':
    unittest.main()



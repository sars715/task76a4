# !/usr/bin/env python
# encoding: utf-8
import unittest
import source


class mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(source.f_11f13a9(1,2,3,4,5,6),4,'fail')
if __name__ == '__main__':
    unittest.main()
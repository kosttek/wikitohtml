'''
Created on 14-05-2012

@author: Pepcok
'''
import unittest
import wikipack;


class Test(unittest.TestCase):

    fileLoader = None
    def setUp(self):
        self.fileLoader= wikipack.fileLoader()
        self.scanner.loadTree('../data/wikitree2.xml')
    def testFile(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFile']
    unittest.main()
'''
Created on 07-04-2012

@author: kosttek
'''
import unittest
import scanner.ScannerPack

class TestScanner(unittest.TestCase):
    scanner = 0
    def setUp(self):
        self.scanner= scanner.ScannerPack.Scanner()
        self.scanner.loadTree('../data/wikitree.xml')

    def testScanLineApostroph(self):
        ret = self.scanner.scanLine("ala ma 'kota' ale ''kot'' nie ma '''ali mc bill''' tak nie \n");
        self.assertEqual(len(ret), 9, "dlugosc listy")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
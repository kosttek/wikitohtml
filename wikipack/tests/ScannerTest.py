'''
Created on 07-04-2012

@author: kosttek
'''
import unittest
import wikipack.scanner.ScannerPack

class TestScanner(unittest.TestCase):
    scanner = 0
    def setUp(self):
        self.scanner= wikipack.scanner.ScannerPack.Scanner()
        self.scanner.loadTree('../data/wikitree2.xml')

    def testScanLineApostroph(self):
        ret = self.scanner.scanLine("ala ma 'kota' ale ''kot'' nie ma '''ali mc bill'''' tak nie \n");
        self.assertEqual(len(ret), 9, "dlugosc listy")
        
    def testScanLineSingle(self):
        ret = self.scanner.scanLine("numer *a_a~a]a dwa \n");
        self.assertEqual(len(ret), 9, "dlugosc listy")
         
    def testScanLineDoubleSign(self):
        ret = self.scanner.scanLine("alasd [% asd %] asda \n");
        self.assertEqual(len(ret), 5, "dlugosc listy")
    
    def testScanFirstMarkNoMarks(self):
        ret = self.scanner.checkLineStartEndMarks("1234 67\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '', "znacznik listy")
        self.assertEqual(ret[2], '', "znacznik poczatku")
    def testScanFirstMarkNoMarksNoNextLine(self):
        ret = self.scanner.checkLineStartEndMarks("1234 67");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '', "znacznik listy")
        self.assertEqual(ret[2], '', "znacznik poczatku")
    def testScanFirstMarkFirstMark(self):
        ret = self.scanner.checkLineStartEndMarks("#1234 67\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '', "znacznik listy")
        self.assertEqual(ret[2], '#', "znacznik poczatku")
        ret = self.scanner.checkLineStartEndMarks("##1234 67\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '', "znacznik listy")
        self.assertEqual(ret[2], "##", "znacznik poczatku")
        ret = self.scanner.checkLineStartEndMarks("###1234 67\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '', "znacznik listy")
        self.assertEqual(ret[2], "###", "znacznik poczatku")
    def testScanFirstMarkFirstMarkLineMark(self):
        ret = self.scanner.checkLineStartEndMarks("#=1234 67=\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '=', "znacznik listy")
        self.assertEqual(ret[2], '#', "znacznik poczatku")
        ret = self.scanner.checkLineStartEndMarks("##==1234 67==\n");
        self.assertEqual(len(ret[0]), 7, "dlugosc listy")
        self.assertEqual(ret[1], '==', "znacznik listy")
        self.assertEqual(ret[2], "##", "znacznik poczatku")
        ret = self.scanner.checkLineStartEndMarks("###===1234 67====\n");
        self.assertEqual(len(ret[0]), 8, "dlugosc listy")
        self.assertEqual(ret[1], "===", "znacznik listy")
        self.assertEqual(ret[2], "###", "znacznik poczatku")
        ret = self.scanner.checkLineStartEndMarks("###=1234 67==\n");
        self.assertEqual(len(ret[0]), 8, "dlugosc listy")
        self.assertEqual(ret[1], "=", "znacznik listy")
        self.assertEqual(ret[2], "###", "znacznik poczatku")
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
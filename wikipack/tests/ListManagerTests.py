'''
Created on 25-06-2012

@author: Pepcok
'''
import unittest
from wikipack.parser import ListManager


class Test(unittest.TestCase):

    def setUp(self):
        self._lm = ListManager.ListManager()

    def testFindingIndexOfEndingTagWithEmptyListAndEmptyToken(self):
        emptyList = []
        self._lm.loadList(emptyList)
        
        returnedValue = self._lm.findIndexOfEndingTag('')
        expectedValue = 0
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 0')
        
    def testFindingIndexOfEndingTagWithEmptyListAndValidToken(self):
        emptyList = []
        self._lm.loadList(emptyList)
        validToken = "'''"
        
        returnedValue = self._lm.findIndexOfEndingTag(validToken)
        expectedValue = 0
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list and valid token returned not 0')
    
    def testFindingIndexOfEndingTagWithInvalidToken(self):
        list = ['a','b','c', "'''", "'", 'e']
        self._lm.loadList(list)
        InvalidToken = "a'b'"
        
        returnedValue = self._lm.findIndexOfEndingTag(InvalidToken)
        expectedValue = 0
        
        self.assertEqual(returnedValue, expectedValue, 'Invalid token returned not 0')
    
    def testFindingIndexOfEndingTagWithSimpleShortList(self):
        list = ["'''","'''"]
        self._lm.loadList(list)
        validToken = "'''"
        
        returnedValue = self._lm.findIndexOfEndingTag(validToken)
        expectedValue = 1
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 1')
    
    def testFindingIndexOfEndingTagWithTagInsideList(self):
        list = ["a", "b", "'''","c","d"]
        self._lm.loadList(list)
        validToken = "'''"
        
        returnedValue = self._lm.findIndexOfEndingTag(validToken)
        expectedValue = 0
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 0')
        
    def testFindingIndexOfEndingTagWithSimpleLongList(self):
        list = ["'''", "b", "c","'''", "d"]
        self._lm.loadList(list)
        validToken = "'''"
        
        returnedValue = self._lm.findIndexOfEndingTag(validToken)
        expectedValue = 3
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 3')
    
    def testFindingIndexOfEndingTagWith2EndingTags(self):
        list = ["'''", "b", "c","'''", "d", "'''", "e"]
        self._lm.loadList(list)
        validToken = "'''"
        
        returnedValue = self._lm.findIndexOfEndingTag(validToken)
        expectedValue = 5
        
        print "returnedValue:" + str(returnedValue)
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 5')
    
    
    #ListCutting tests
    
    def testListCuttingFromBeginning(self):
        listToCut = ["a", "b", "c","d","e","f"]
        self._lm.loadList(listToCut)
        
        returnedList = self._lm.cutList(0, 3)
        expectedLength = 2
        self.assertEqual(len(returnedList), expectedLength, 'List has wrong length')
        
    def testListCuttingFromMiddle(self):
        listToCut = ["a", "b", "c","d","e","f","g"]
        self._lm.loadList(listToCut)
        
        returnedList = self._lm.cutList(2, 6)
        expectedLength = 3
        self.assertEqual(len(returnedList), expectedLength, 'List has wrong length')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
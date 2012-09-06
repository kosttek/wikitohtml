'''
Created on 25-06-2012

@author: Pepcok
'''
import unittest
from wikipack.parser import ListManager
from wikipack.parser.ListManager import NotATagException


class Test(unittest.TestCase):

    def setUp(self):
        self._lm = ListManager.ListManager()

    def testFindingIndexOfEndingTagWithEmptyListAndEmptyToken(self):
        emptyList = []
        self._lm.loadList(emptyList)
        
        self.assertRaises(NotATagException, self._lm.findIndexOfEndingTag, '')
        
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
        
        self.assertRaises(NotATagException, self._lm.findIndexOfEndingTag, InvalidToken)
    
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
        expectedValue = 3
        
        #print "returnedValue:" + str(returnedValue)
        
        self.assertEqual(returnedValue, expectedValue, 'Empty list  and empty token returned not 3')
    
    
    #ListCutting tests
    
    def testFindingIndexOfEndingTagWithSemicolonAtBeginningWithoutNewLine(self):
        testList = [";", "a", "b", "c"]
        self._lm.loadList(testList)
        token = ";"
        returnedValue = self._lm.findIndexOfEndingTag(token)
        expectedValue = 3
        
        self.assertEqual(returnedValue, expectedValue, 'Semiconon at beginning without new line returned '+str(returnedValue)+', not '+str(expectedValue))
        
    def testFindingIndexOfEndingTagWithSemicolonAtBeginningWitNewLine(self):
        testList = [";", "a", "b", "c","\n", "d", "e"]
        self._lm.loadList(testList)
        token = ";"
        returnedValue = self._lm.findIndexOfEndingTag(token)
        expectedValue = 4
        
        self.assertEqual(returnedValue, expectedValue, 'Semiconon at beginning without new line returned '+str(returnedValue)+' not '+str(expectedValue))
        
    def testFindingIndexOfEndingTagWithSemicolonInMiddle(self):
        testList = ["1", ";", "a", "b", "c"]
        self._lm.loadList(testList)
        token = ";"
        
        self.assertRaises(NotATagException, self._lm.findIndexOfEndingTag,token)
    
        
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
                
    def testFindingIndexOfEndingTagInLink(self):
        testList = ["a","[[", "c", "'", "]]", "]]"]
        self._lm.loadList(testList)
        token = "[["
        expectedValue = 4
        
        returnedValue = self._lm.findIndexOfEndingTag(token)
        self.assertEqual(returnedValue, expectedValue, 'Link: wrong number of ending tag. Expected '+str(expectedValue)+', got ' +str(returnedValue))
    

    def testFindingIndexOfEndingTagWithValidSemicolonInMiddle(self):
        testList = ["1",'b', '\n' ';', "a", 'b', '\n',"c"]
        self._lm.loadList(testList)
        token = ";"
        returnedValue = self._lm.findIndexOfEndingTag(token)
        expectedValue = 6
        
        self.assertEqual(returnedValue, expectedValue, 'Semiconon at beginning without new line returned '+str(returnedValue)+' not '+str(expectedValue))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
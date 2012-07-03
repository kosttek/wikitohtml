'''
Created on 19-05-2012

@author: Pepcok
'''
from xml.etree.ElementTree import ElementTree
import os

class ParserTreeHelper(object):
    
    __xmlTreePath = 'parserTree.xml'
    __tokenTree = None


    def __init__(self):
        self.__tokenTree = ElementTree()
        self.__tokenTree.parse(os.path.dirname(__file__) + '\\' + self.__xmlTreePath)
        
    def isTokenATag(self, tokenSymbol):
        tokenList = self.__tokenTree.findall('token')
        for token in tokenList:
            if tokenSymbol == token.find('startTag').text:
                return True
        return False;
    
    def getEndingTag(self, tokenSymbol):
        if not self.isTokenATag(tokenSymbol):
            return None
        tokenList = self.__tokenTree.findall('token')
        for token in tokenList:
            startTag = token.find('startTag').text
            endingTag = token.find('startTag').text
            if tokenSymbol == startTag:
                return endingTag if (endingTag != "") else None
        return None
    
    
    #todo test
    def getTagId(self, tokenSymbol):
        if not self.isTokenATag(tokenSymbol):
            return None
        tokenList = self.__tokenTree.findall('token')
        for token in tokenList:
            startTag = token.find('startTag').text
            name = token.find('id').text
            if tokenSymbol == startTag:
                return name 
        return None
    
    def affectsLine(self, tokenSymbol):
        if not self.isTokenATag(tokenSymbol):
            return False
        tokenList = self.__tokenTree.findall('token')
        for token in tokenList:
            startTag = token.find('startTag').text
            if startTag == tokenSymbol:
                if token.find('affects').text == "line":
                    return True
                return False
        return False
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
   parser = ParserTreeHelper()
   parser.isTokenATag("'''")

from wikipack.parser.ParserTreeHelper import ParserTreeHelper
from xml.etree.ElementTree import Element


class ListManager(object):
    
    __list = None
    __pth = None
    __debug = None
    
    def __init__(self):
        self.__pth = ParserTreeHelper()
        self.__debug = False

    @staticmethod
    def clearListFromEmptyTokens(tokenList):
        whiteTokensCount = tokenList.count('')
        for i in range(whiteTokensCount):
            tokenList.pop(tokenList.index(''))
        return tokenList
    
    def loadList(self, list):
        self.__list = list

    #TODO test    
    def findIndexOfEndingTag(self, token):
        if not self.__pth.isTokenATag(token):
            return 0
        endingTag = self.__pth.getEndingTag(token)
        expectedIndexOfEndingTag = 0
        sameTagCount = 0
        if self.__debug:
            print "endingtag: " + endingTag
            print "expected index: " + str(expectedIndexOfEndingTag)
            print "same Tag Count: " + str(sameTagCount)
            
        for idx, currentTokenElement in enumerate(self.__list):
            None
            #first element is our token and should not be considered as potential ending tag
            if idx == 0:
                continue
            
            if currentTokenElement == token:
                sameTagCount = sameTagCount +1 
            if currentTokenElement == endingTag:
                expectedIndexOfEndingTag = idx
                sameTagCount = sameTagCount - 1 
         
            if sameTagCount < 0:
                break
            
        return expectedIndexOfEndingTag
    
    #todo test
    def parseListToElement(self):
        headElement = Element()

        for i in len(self.__list):
            currentToken = self.__list[i]
            newElement = Element()  
            if not self.__pth.isTokenATag(currentToken):
                newElement.set('name', 'text')
                newElement.text = currentToken
            
            endingTagIndex = self.findIndexOfEndingTag(currentToken)
            
            if endingTagIndex == 0:
                newElement.set('name', 'text')
                newElement.text = currentToken
            
            currentTokenName = self.__pth.getTagId(currentToken)
            tokenElement = Element()
            tokenElement.set('name', currentTokenName)
            
            #todo wycinanie listy
            
            headElement.append(tokenElement)
            
            return headElement
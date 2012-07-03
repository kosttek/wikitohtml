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
        skipFirstOccurenceOfTag = False
        if token == endingTag:
            skipFirstOccurenceOfTag = True
        
        for idx, currentTokenElement in enumerate(self.__list):
            None
            if currentTokenElement == token:
                if skipFirstOccurenceOfTag:
                    skipFirstOccurenceOfTag = False
                    continue
                else:
                    sameTagCount += 1 
            if currentTokenElement == endingTag:
                expectedIndexOfEndingTag = idx
                sameTagCount -= 1
                
                     
         
            if sameTagCount < 0:
                break
            
        return expectedIndexOfEndingTag
    
    #todo test
    def parseListToElement(self):
        headElement = Element("headElement")
        skip = None

        for i, currentToken in enumerate(self.__list):
            
            if i < skip:
                continue
            
            newElement = Element("token")  
            if not self.__pth.isTokenATag(currentToken):
                newElement.set('name', 'text')
                newElement.text = currentToken
            
            else:
                endingTagIndex = self.findIndexOfEndingTag(currentToken)
            
                if endingTagIndex == 0:
                    newElement.set('name', 'text')
                    newElement.text = currentToken
                else:
                    currentTokenName = self.__pth.getTagId(currentToken)
                    newElement.set('name', currentTokenName)
                
                    trimmedList = self.cutList(i, endingTagIndex)
                    tmpListManger = ListManager()
                    tmpListManger.loadList(trimmedList)
                    returnedElement = tmpListManger.parseListToElement()
                    newElement.append(returnedElement)
                    
                    skip = endingTagIndex
                    
            headElement.append(newElement)
            
        return headElement
        
    def cutList(self, startingIndex, endingIndex):
        return self.__list[startingIndex+1 : endingIndex]
        
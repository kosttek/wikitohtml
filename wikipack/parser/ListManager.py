from wikipack.parser.ParserTreeHelper import ParserTreeHelper
from xml.etree.ElementTree import Element

class NotATagException(BaseException):
    pass

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
            raise NotATagException
        specialRequirement = self.__pth.getSpecialRequirements(token) 
        endingTag = self.__pth.getEndingTag(token)
        expectedIndexOfEndingTag = 0
        skipFirstOccurenceOfTag = False
        if token == endingTag:
            skipFirstOccurenceOfTag = True
        counter = 0
        start_token_found = False
        for idx, currentTokenElement in enumerate(self.__list):
            counter = idx
            
            if currentTokenElement == token:
                start_token_found = True
                if specialRequirement == 'FirstInLine':
                    if idx != 0:
                        if self.__list[idx-1] != '\n':
                            raise NotATagException
            if (currentTokenElement == endingTag) and start_token_found:
                if skipFirstOccurenceOfTag:
                    skipFirstOccurenceOfTag = False
                    continue
                else:
                    expectedIndexOfEndingTag = idx
                    break
        if self.__pth.affectsLine(token):
            return counter
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
                try:
                    endingTagIndex = self.findIndexOfEndingTag(currentToken)
                except NotATagException:
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
        
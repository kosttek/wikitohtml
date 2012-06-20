from wikipack.parser.ParserTreeHelper import ParserTreeHelper

class ListManager(object):
    
    __list = None
    __pth = None
    
    def __init__(self):
        self.__pth = ParserTreeHelper()

    @staticmethod
    def clearListFromEmptyTokens(tokenList):
        whiteTokensCount = tokenList.count('')
        for i in range(whiteTokensCount):
            tokenList.pop(tokenList.index(''))
        return tokenList
    
    def loadList(self, list):
        self.__list = list
    
    def findIndexOfEndingTag(self, token):
        if not self.__pth.isTokenATag(token):
            return 0
        #TODO
        for idx, tokenElement in enumerate(self.__list):
            
            
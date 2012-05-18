'''
Created on 19-05-2012

@author: Pepcok
'''

class ListManager(object):

    @staticmethod
    def clearListFromEmptyTokens(tokenList):
        whiteTokensCount = tokenList.count('')
        for i in range(whiteTokensCount):
            tokenList.pop(tokenList.index(''))
        return tokenList
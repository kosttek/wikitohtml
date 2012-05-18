'''
Created on 25-04-2012

@author: Pepcok
'''

class fileLoader:
    
    fileHandler = None


    def __init__(self):
        '''
        Constructor
        '''
    def loadFile(self, filename):
        self.fileHandler = open('../test/PepcokTests/' + filename + '.txt');
    
    def printFile(self):
        print self.fileHandler.read()
    
    def getFileContent(self):
        return self.fileHandler.read()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    fl = fileLoader()
    fl.loadFile('firstTest')
    fl.printFile()
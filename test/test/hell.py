'''
Created on 16-03-2012

@author: kosttek
'''
import sys
from xml.etree.ElementTree import ElementTree

class LoadFile:
    def read(self,path):
        try:
            f = open(path,'r')
            print f
        except IOError:
            print 'There is no file like this, Joseph is disappointed'
            
    def readXMLosoby(self):
        tree = ElementTree()
        tree.parse('../data/some_data.xml')
        root = tree.getroot()
        print dir(root)
        osoby = root.iter('osoba')
        for osoba in osoby:
            print osoba.attrib
            for dane in osoba.iter():
                print dane.tag, dane.text,  dane.iter()
                
    def readXML2(self):
        tree = ElementTree()
        tree.parse('../data/wikitree.xml')
        root = tree.getroot()
        print dir(root)
        elemelki = list(root)
        for elemelek in elemelki:
            print elemelek

class Scanner:
    tree = 0
    file = 0
    treeElement = 0
    
    def loadTree(self,path):
        self.tree = ElementTree()
        self.tree.parse(path)
    
    def loadFile(self,path):
        self.file = open(path,'r')
        
    def scan(self):
        treeElement = self.tree.getroot()
        for character in self.file.read() :
            print character
        # stack .pop() .append()
        # trzeba ogarniac czy znacznik jest juz zamkniety czy jeszcze nie niestety

if __name__ == '__main__':
    scanner = Scanner()
    scanner.loadTree('../data/wikitree.xml')
    scanner.loadFile('../data/testfile')
    scanner.scan()
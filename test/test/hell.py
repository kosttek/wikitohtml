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
        for line in self.file.readlines() :
            #print line 
            print self.checkLineStartEndMarks(line)    

    def checkLineStartEndMarks(self,line):
        if len(line)>2:
            treeElement = self.tree.getroot()
            for element in treeElement.iter("linemark"): 
                if element.attrib['value'] == line[0] and element.attrib['value'] == line[-2]:
                    mark = element.attrib['value']
                    for i in range(1,int(element.attrib['max'])):
                        if mark == line[i] and mark == line[-2-i]:
                            pass
                        else:
                            return {i, mark}
        return {0,""}
    
if __name__ == '__main__':
    scanner = Scanner()
    scanner.loadTree('../data/wikitree.xml')
    scanner.loadFile('../data/testfile')
    scanner.scan()
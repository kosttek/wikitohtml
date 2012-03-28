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
        osoby = root.iter('osoba')
        for osoba in osoby:
            print osoba.attrib
            for dane in osoba.iter():
                print dane.tag, dane.text,  dane.iter()

if __name__ == '__main__':
    print 'hell'
    print sys.__class__
    x = LoadFile()
    x.readXMLosoby()
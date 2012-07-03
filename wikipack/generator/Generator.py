'''
Created on 03-07-2012

@author: kosttek
'''
import sys
from xml.etree.ElementTree import ElementTree

class Generator(object):
    '''
    classdocs
    '''
    def generate(self,elementstart):
        result = ''
        for elem in list(elementstart):
            if elem.get('name') == 'text':
                result += elem.text
            else:
                tags = self.getTags(elem.get('name'))
                result += tags[0]
                result += self.generate(elem)
                result += tags[1]
        return result

        
    def getTags(self,name):
        if name == 'bold':
            return ['<b>','</b>']
        else:
            return {'',''}

if __name__ == '__main__':
    path = 'file.xml'
    tree = ElementTree()
    tree.parse(path)
 #   print list(tree.getroot().iter().next())
 #   print list(tree.iter().next())
 #   print tree.getroot().iter().next()
 #   for elem in list(tree.getroot()):
 #       print elem.get('name')
 
gen = Generator()
print gen.generate(tree.getroot())
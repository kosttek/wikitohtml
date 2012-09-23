'''
Created on 21-09-2012

@author: kosttek
'''
from xml.dom.minidom import Document

class SpecialParse:
    def parse(self,parser):
        return [Document().createElement("br"),1]
    
'''
Created on 30-06-2012

@author: Pepcok
'''
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

window = Element("window")

title = SubElement(window, "title", font="large")
title.text = "A sample text window"

text = SubElement(window, "text", wrap="word")

box = SubElement(window, "buttonbox")
SubElement(box, "button").text = "OK"
SubElement(box, "button").text = "Cancel"


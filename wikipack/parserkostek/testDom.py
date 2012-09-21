'''
Created on 07-04-2012

@author: kosttek
'''

from xml.dom.minidom import Document

# Create the minidom document
doc = Document()

# Create the <wml> base element
wml = doc.createElement("wml")
doc.appendChild(wml)

# Create the main <card> element
maincard = doc.createElement("card")
maincard.setAttribute("id", "main")
wml.appendChild(maincard)

# Create a <p> element
paragraph1 = doc.createElement("p")
maincard.appendChild(paragraph1)
paragraph2 = doc.createElement("p")
#maincard.appendChild(paragraph2)



# Give the <p> elemenet some text
ptext = doc.createTextNode("This is a test!")
ptext2 = doc.createTextNode("This is a sparta!")
ptext3 = doc.createTextNode("This is a agh!")
paragraph1.appendChild(ptext3)
paragraph1.appendChild(ptext)
paragraph2.appendChild(ptext2)
paragraph1.appendChild(paragraph2)



# Print our newly created XML
print doc.toprettyxml(indent=" ")
p = maincard.getElementsByTagName("*")[0]
print p.childNodes[0]._get_nodeValue()
#ptext._
# -*- coding: UTF-8 -*-
# transfer other type file to xml or generate a xml file
from xml.etree.ElementTree import ElementTree, Element, tostring
elem_root = Element("STOCK")
tostring(elem_root)
# set attribute
#  '<data name="2017-01-26" />'
elem_root.set("code", u"600000")
# set text of element
# '<data name="2017-01-26">hello, world</data>'
elem_root.text = "PFYH"
tostring(elem_root)
# add elem_data as the son element of element elem_root
elem_date = Element("DATE")
elem_date.text = "2017-01-26"
# '<STOCK code="600000">PFYH<DATE>2017-01-26</DATE></STOCK>'
elem_root.append(elem_date)

# write element tree to file
elem_tree = ElementTree(elem_root)
elem_tree.write("1.xml")



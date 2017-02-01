# xml file IO
from xml.etree.ElementTree import parse
# open a xml file
xml_f = open("demo.xml", "rw")
# p type: <xml.etree.ElementTree.ElementTree at 0x10248b9d0>
p = parse(xml_f)
# get root node of an xml file
# root_node: <Element 'CATALOG' at 0x10248b550>
root_node = p.getroot()
"""
  root_node.append      root_node.find        root_node.getiterator
  root_node.attrib      root_node.findall     root_node.insert
  root_node.clear       root_node.findtext    root_node.items
  root_node.copy        root_node.get         root_node.iter
  root_node.extend      root_node.getchildren root_node.iterfind
  ...
"""
# 'CATALOG'
root_node.tag
# {}
root_node.attrib
# [<Element 'CD' at 0x10248b910>, <Element 'CD' at 0x10248ba50>], will remove in future python xml module edition
root_node.getchildren()
# use for to retrieve every child
for child in root_node:
    print child.get("NAME")
# filter by label: <Element 'CD' at 0x1024d95d0>
# the first one
root_node.find("CD")
# get all elements by filtering with label
# [<Element 'CD' at 0x1024d95d0>, <Element 'CD' at 0x1024d9850>]
root_node.findall("CD")
# sometimes we do not want to return a list but a generator
# <generator object select at 0x1024ac690>
root_node.iterfind("CD")

# the above examples which use find alike functions are only get children items
# if u want to find any item, could use iter
# <Element 'TITLE' at 0x1024d9890>, <Element 'TITLE' at 0x1024d9b10>
root_node.iter('TITLE')
# [<Element 'TITLE' at 0x1024d9890>, <Element 'TITLE' at 0x1024d9b10>]
list(root_node.iter('TITLE'))

# all grandson item nodes, use "${childnode}/*"
"""
[<Element 'TITLE' at 0x1024d9890>,
 <Element 'ARTIST' at 0x1024d9590>,
 <Element 'COUNTRY' at 0x1024d9790>,
 <Element 'COMPANY' at 0x1024d9950>,
 <Element 'PRICE' at 0x1024d99d0>,
 <Element 'YEAR' at 0x1024d9a90>,
 <Element 'TITLE' at 0x1024d9b10>,
 <Element 'ARTIST' at 0x1024d97d0>,
 <Element 'COUNTRY' at 0x1024d96d0>,
 <Element 'COMPANY' at 0x1024d9a50>,
 <Element 'PRICE' at 0x1024d9ad0>,
 <Element 'YEAR' at 0x1024d9b50>]
"""
root_node.findall("CD/*")

# ether element contains COUNTRY item
# [<Element 'COUNTRY' at 0x1024d9790>, <Element 'COUNTRY' at 0x1024d96d0>]
root_node.findall(".//COUNTRY")

# ".." to find father item element
# find father element which have child element of COUNTRY
# [<Element 'CD' at 0x1024d95d0>, <Element 'CD' at 0x1024d9850>]
root_node.findall(".//COUNTRY/..")

# filter element has certain attribute
# [<Element 'CD' at 0x1024d95d0>, <Element 'CD' at 0x1024d9850>]
root_node.findall("CD[@NAME]")
# <Element 'CD' at 0x1024d9850>
# filter by element attribute
root_node.find('CD[@NAME="Hide your heart"]')
# filter by element son attribute
root_node.find('CD[COMPANY="Columbia"]')

# filter element by position
root_node.findall(".//COUNTRY/..[1]")
root_node.findall(".//COUNTRY/..[last]")
xml_f.close()
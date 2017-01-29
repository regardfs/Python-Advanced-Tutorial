import csv
from xml.etree.ElementTree import Element, ElementTree, tostring


def csv_to_xml(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        header = reader.next()              # every element in headers should be the tag of the xml file
        elem_root = Element("STOCK")
        elem_root.set("code", u"600000")
        elem_root.text = "PFYH"
        for row in reader:
            elem_row = Element("ROW")
            elem_root.append(elem_row)
            for tag, text in zip(header, row):
                elem_tag = Element(tag)
                elem_tag.text = text
                elem_row.append(elem_tag)
    xml_format(elem_root)
    return ElementTree(elem_root)


def xml_format(elem, level=0):
    if len(elem) > 0:
        elem.text = '\n' + ' ' * level
        for child in elem:
            xml_format(child, level+1)
        child.tail = child.tail[:-1]
    elem.tail = '\n' + '\t' * level


def main(original_file, target_file):
    elem_tree = csv_to_xml(original_file)
    elem_tree.write(target_file)


if __name__ == "__main__":
    main("600000.csv", "600000.xml")
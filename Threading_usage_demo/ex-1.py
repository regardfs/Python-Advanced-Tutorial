import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from cStringIO import StringIO

from threading import Thread


def csv_to_xml(csvfd, xmlfd):
    reader = csv.reader(csvfd)
    header = reader.next()
    elem_root = Element("STOCK")
    for row in reader:
        elem_row = Element("ROW")
        elem_root.append(elem_row)
        for tag, text in zip(header, row):
            elem_tag = Element(tag)
            elem_tag.text = text
            elem_row.append(elem_tag)
    xml_format(elem_root)
    et = ElementTree(elem_root)
    et.write(xmlfd)


def xml_format(elem, level=0):
    if len(elem) > 0:
        elem.text = '\n' + '\t' * (level + 1)
        for child in elem:
            xml_format(child, level+1)
        child.tail = child.tail[:-1]
    elem.tail = '\n' + '\t' * level


def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)


# only helpful in IO intensive mode
# other than CPU intensive mode due
# to global interpreter lock(GIL)
class XmlHandleThreading(Thread):
    def __init__(self, sid):
        super(XmlHandleThreading, self).__init__()
        self.sid = sid

    def handle(self):
        url = "http://table.finance.yahoo.com/table.csv?s=6%s.ss"
        url %= str(self.sid).rjust(5, '0')
        print url
        print "download...(6%s)" % str(self.sid).rjust(5, '0')
        dl = download(url)
        if dl is None:
            return
        print "Convert to xml for code of 6%s" % str(self.sid).rjust(5, '0')
        xml_file = "6%s.xml" % str(self.sid).rjust(5, '0')
        with open(xml_file, 'wb') as xml_fd:
            csv_to_xml(dl, xml_fd)

    def run(self):
        self.handle()


threads = []
for s in xrange(0, 11):
    t = XmlHandleThreading(s)
    threads.append(t)
    t.start()

for t in threads:
    t.join()


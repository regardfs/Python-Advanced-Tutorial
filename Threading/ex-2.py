import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from cStringIO import StringIO

from threading import Thread
from Queue import Queue


class DownloadThread(Thread):

    def __init__(self, sid, queue):
        super(DownloadThread, self).__init__()
        self.sid = sid
        self.queue = queue
        self.url = "http://table.finance.yahoo.com/table.csv?s=6%s.ss" %  str(self.sid).rjust(5, '0')

    def download(self):
        response = requests.get(self.url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        # 1. download
        print "Download...(%s)" % self.sid
        csv_data = self.download()
        # 2. send download to convert thread
        # should lock in case of concurrent visit d_que or we could use Queue.Queue
        self.queue.put((self.sid, csv_data))


class ConvertThread(Thread):

    def __init__(self, queue):
        super(ConvertThread, self).__init__()
        self.queue = queue

    def xml_format(self, elem, level=0):
        if len(elem) > 0:
            elem.text = '\n' + '\t' * (level + 1)
            for child in elem:
                self.xml_format(child, level + 1)
            child.tail = child.tail[:-1]
        elem.tail = '\n' + '\t' * level

    def csv_to_xml(self, csvfd, xmlfd):
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
        self.xml_format(elem_root)
        et = ElementTree(elem_root)
        et.write(xmlfd)

    def run(self):
        while True:
            sid, data = self.queue.get()
            print "convert...(%s)" % sid
            if sid == -1:
                break
            if data:
                xml_file = "6%s.xml" % str(sid).rjust(5, '0')
                with open(xml_file, 'wb') as xml_fd:
                    self.csv_to_xml(data, xml_fd)

que = Queue()
dThreads = [DownloadThread(i, que) for i in xrange(0, 11)]
cThread = ConvertThread(que)

for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()

que.put((-1, None))


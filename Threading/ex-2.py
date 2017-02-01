# we could use Queue.Queue data structure shared by several Threads for communication
# we could use Event which obtained by several Threads for communication

import csv
import tarfile
import os
import requests

from xml.etree.ElementTree import Element, ElementTree
from cStringIO import StringIO
from threading import Thread, Event
from Queue import Queue


class TarThread(Thread):

    def __init__(self, c_event, t_event):
        super(TarThread, self).__init__()
        self.count = 0
        self.c_event = c_event
        self.t_event = t_event
        self.setDaemon(True)    # set this thread process as Daemon process

    def tar_file(self, mode="w:gz", ob_path=".", pattern=None):
        tar_filename = "%s.tgz" % (self.count + 1)
        try:
            tf = tarfile.open(tar_filename, mode)
            for fn in os.listdir(ob_path):
                if fn.endswith(pattern):
                    tf.add(fn)
            tf.close()
            if not tf.members:
                os.remove(tar_filename)
        except Exception as e:
            print "Failed to tarfile due to: %s" % e
        else:
            self.count += 1

    def run(self):
        while True:
            self.c_event.wait()
            self.tar_file(pattern=".xml")
            self.c_event.clear()
            self.t_event.set()


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

    def __init__(self, queue, c_event, t_event):
        super(ConvertThread, self).__init__()
        self.queue = queue
        self.c_event = c_event
        self.t_event = t_event

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
        count = 0
        while True:
            sid, data = self.queue.get()
            print "convert...(%s)" % sid
            if sid == -1:
                self.c_event.set()
                self.t_event.wait()
                break
            if data:
                xml_file = "6%s.xml" % str(sid).rjust(5, '0')
                with open(xml_file, 'wb') as xml_fd:
                    self.csv_to_xml(data, xml_fd)
                count += 1
                if count == 5:
                    self.c_event.set()
                    self.t_event.wait()
                    self.t_event.clear()
                    count = 0


if __name__ == "__main__":
    que = Queue()

    dThreads = [DownloadThread(i, que) for i in xrange(0, 11)]

    # or, we could use threading.lock() to set a single lock, but in this case, we use Event() as our lock
    # lk = threading.lock()
    # lk.acquire([timeout])  # lock !!!
    # lk.release() # release lock !!!

    c_event = Event()
    t_event = Event()

    cThread = ConvertThread(que, c_event, t_event)

    tThread = TarThread(c_event, t_event)
    tThread.start()

    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()

    que.put((-1, None))

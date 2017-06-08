#!/usr/bin/env python

import os
import logging
from logging.handlers import RotatingFileHandler


class EtcdLogger(object):

    def __init__(self, loggername= "EtcdLog",
                 filename='./var/log/etcd/etcdop.log',
                 format="[%(asctime)s] %(filename)s [%(levelname)s] %(message)s"):

        self.loggername = loggername
        self.filename = filename
        self.format = format

    def logger_init(self):

        self.logdir_init()

        formatter = logging.Formatter(self.format)

        logger = logging.getLogger(self.loggername)
        logger.setLevel(level=logging.INFO)

        rHandler = RotatingFileHandler(self.filename, maxBytes=1 * 1024, backupCount=3)
        rHandler.setLevel(logging.INFO)

        rHandler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        logger.addHandler(rHandler)
        logger.addHandler(console)

        return logger

    def logdir_init(self):

        filedir = "/".join([key for key in self.filename.split("/")[:-1]])

        if not os.path.exists(filedir):
            os.makedirs(filedir)












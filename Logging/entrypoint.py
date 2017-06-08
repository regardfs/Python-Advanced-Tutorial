from log_test1 import Test1
from log_test2 import Test2
from logging_demo import EtcdLogger

if __name__=='__main__':

    logger = EtcdLogger().logger_init()

    t1 = Test1(logger).pl()
    t2 = Test2(logger).pl()
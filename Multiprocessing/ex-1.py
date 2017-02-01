from multiprocessing import Pipe, Queue, Process

q = Queue()

q.put(1)
q.get()


def func_1(q):
    print "start"
    print q.get()
    print "end"

Process(target=func_1, args=(q,)).start()


def func_2(p):
    p.send(p.recv() ** 2)

p1, p2 = Pipe()


Process(target=func_2, args=(p2, )).start()

p1.send(10)
p1.recv()



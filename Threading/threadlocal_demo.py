# threading parameter isolation
# create a threading.local() type parameter
# https://github.com/pallets/werkzeug/blob/8a84b62b3dd89fe7d720d7948954e20ada690c40/werkzeug/local.py

"""Thread-local objects usage

(Note that this module provides a Python version of the threading.local
 class.  Depending on the version of Python you're using, there may be a
 faster one available.  You should always import the `local` class from
 `threading`.)

Thread-local objects support the management of thread-local data.
If you have data that you want to be local to a thread, simply create
a thread-local object and use its attributes:

#   >>> mydata = local()
#   >>> mydata.number = 42
#   >>> mydata.number
#   42
#
# You can also access the local-object's dictionary:
#
#   >>> mydata.__dict__
#   {'number': 42}
#   >>> mydata.__dict__.setdefault('widgets', [])
#   []
#   >>> mydata.widgets
#   []
#
# What's important about thread-local objects is that their data are
# local to a thread. If we access the data in a different thread:
#
#   >>> log = []
#   >>> def f():
#   ...     items = mydata.__dict__.items()
#   ...     items.sort()
#   ...     log.append(items)
#   ...     mydata.number = 11
#   ...     log.append(mydata.number)
#
#   >>> import threading
#   >>> thread = threading.Thread(target=f)
#   >>> thread.start()
#   >>> thread.join()
#   >>> log
#   [[], 11]
#
# we get different data.  Furthermore, changes made in the other thread
# don't affect data seen in this thread:
#
#   >>> mydata.number
#   42
#
# Of course, values you get from a local object, including a __dict__
# attribute, are for whatever thread was current at the time the
# attribute was read.  For that reason, you generally don't want to save
# these values across threads, as they apply only to the thread they
# came from.
#
# You can create custom local objects by subclassing the local class:
#
#   >>> class MyLocal(local):
#   ...     number = 2
#   ...     initialized = False
#   ...     def __init__(self, **kw):
#   ...         if self.initialized:
#   ...             raise SystemError('__init__ called too many times')
#   ...         self.initialized = True
#   ...         self.__dict__.update(kw)
#   ...     def squared(self):
#   ...         return self.number ** 2
#
# This can be useful to support default values, methods and
# initialization.  Note that if you define an __init__ method, it will be
# called each time the local object is used in a separate thread.  This
# is necessary to initialize each thread's dictionary.
#
# Now if we create a local object:
#
#   >>> mydata = MyLocal(color='red')
#
# Now we have a default number:
#
#   >>> mydata.number
#   2
#
# an initial color:
#
#   >>> mydata.color
#   'red'
#   >>> del mydata.color
#
# And a method that operates on the data:
#
#   >>> mydata.squared()
#   4
#
# As before, we can access the data in a separate thread:
#
#   >>> log = []
#   >>> thread = threading.Thread(target=f)
#   >>> thread.start()
#   >>> thread.join()
#   >>> log
#   [[('color', 'red'), ('initialized', True)], 11]
#
# without affecting this thread's data:
#
#   >>> mydata.number
#   2
#   >>> mydata.color
#   Traceback (most recent call last):
#   ...
#   AttributeError: 'MyLocal' object has no attribute 'color'
#
# Note that subclasses can define slots, but they are not thread
# local. They are shared across threads:
#
#   >>> class MyLocal(local):
#   ...     __slots__ = 'number'
#
#   >>> mydata = MyLocal()
#   >>> mydata.number = 42
#   >>> mydata.color = 'red'
#
# So, the separate thread:
#
#   >>> thread = threading.Thread(target=f)
#   >>> thread.start()
#   >>> thread.join()
#
# affects what we see:
#
#   >>> mydata.number
#   11
#
# >>> del mydata


# >>> below is the core code of threading.local()
def _patch(self):
    key = object.__getattribute__(self, '_local__key')  #
    d = current_thread().__dict__.get(key)  #
    if d is None:
        d = {}
        current_thread().__dict__[key] = d
        object.__setattr__(self, '__dict__', d)

        # we have a new instance dict, so call out __init__ if we have one
        cls = type(self)
        if cls.__init__ is not object.__init__:
            args, kw = object.__getattribute__(self, '_local__args')
            cls.__init__(self, *args, **kw)
    else:
        object.__setattr__(self, '__dict__', d)

"""

import threading

global_data = threading.local()


def show():
    print threading.current_thread().getName(), global_data.num


def thread_cal():
    global_data.num = 0
    for _ in xrange(1000):
        global_data.num += 1
    show()


threads = []

for i in xrange(10):
    t = threading.Thread(target=thread_cal)
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print "Main thread: ", global_data.__dict__  # {}


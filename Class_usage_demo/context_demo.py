"""
A useful example could be a database connection object (which then automagically closes the connection once the
corresponding 'with'-statement goes out of scope):

class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.db_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.db_conn.close()
        # return True if you want shield the exception generate by any function
        ...
As explained above, use this object with the with statement (you may need to do from __future__ import with_statement
at the top of the file if you're on Python 2.5).

with DatabaseConnection() as mydbconn:
    # do stuff

"""

# https://www.python.org/dev/peps/pep-0343/


# an example
class Context(object):

    def __enter__(self):
        print "entering the zone"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "leaving the zone"
        if exc_type is None:
            print "with no error"
        else:
            print "with an error (%s)" % exc_val

# test 1: no exception
with Context():
    print "i am in the normal zone"

# test 2: exception
with Context():
    print "i am in the Exception zone"
    raise TypeError("Exception zone test")


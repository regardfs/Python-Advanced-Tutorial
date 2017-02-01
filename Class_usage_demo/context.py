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


# This module implements a file-like class, StringIO and cStringIO, that reads and writes a string buffer
# (also known as memory files). See the description of file objects for operations (section File Objects).
# (For standard strings, see str and unicode.)

# https://docs.python.org/2/library/stringio.html

# StringIO
import StringIO

output = StringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

# cStringIO
import cStringIO

output = cStringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
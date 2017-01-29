# usage of temp file, especially in scenario of large file IO

from tempfile import TemporaryFile, NamedTemporaryFile
# create a temporary file without name, thus could not find it in your system
f1 = TemporaryFile()
f1.write("!@#123xyz" * 10000)
# then to the start position of the file
f1.seek(0)
# read content of the file by fd: f1
f1.read(300)

# create a named temporary file, automatically delete when close
# /var/folders/sf/k9dtdgx14dj8c0q7g01w7wsr0000gn/T/``filename``
f2 = NamedTemporaryFile()
# automatically delete when close()
f2.close()



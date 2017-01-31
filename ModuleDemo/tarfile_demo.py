import tarfile
import os


# usage: tar_file("test.gz",pattern=".xml")
def tar_file(tar_filename=None, mode="w:gz", ob_path=".", pattern=None):
    try:
        tf = tarfile.open(tar_filename, mode)
        for fn in os.listdir(ob_path):
            if fn.endswith(pattern):
                tf.add(fn)
                os.remove(fn)
        tf.close()

        if not tf.members:
            os.remove(tar_filename)
    except Exception as e:
        print "Failed to tarfile due to: %s" % e


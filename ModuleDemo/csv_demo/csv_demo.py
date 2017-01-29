# *.csv file IO demo
# use csv module
import csv
# download csv file
from urllib import urlretrieve
urlretrieve("http://table.finance.yahoo.com/table.csv?s=600000.ss", "600000.csv")
f1 = open("600000.csv", "rb")
# csv.reader(fd) return a generater
f1_reader = csv.reader(f1)
f1_reader.next()
f1_reader.next()
f1.close()

# below scope code demonstrates how to operate csv type file
with open("600000.csv", "rb") as original_600000:
    # use csv.reader to read csv file, return a Iterator, we could access by for/next()
    f1_reader = csv.reader(original_600000)
    with open("conditional_600000.csv", "wb") as conditional_600000:
        # use csv.write to write to csv file
        f1_write = csv.writer(conditional_600000)
        f1_write.writerow(f1_reader.next())
        for data in f1_reader:
            if data[0] > '2017-01-01' and int(data[5]) >= 30000000:
                f1_write.writerow(data)


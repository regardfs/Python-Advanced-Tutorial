# For python3 env

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, month, day) = data

s = "hello"
a, b, c, d, e = s

# use _ for position occupy
_, shares, price, _ = data

# use * for iteration
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# [10, 8, 7, 1, 9, 5, 10]
print(trailing)

tems = [1, 10, 7, 4, 5, 9]
head, *tail = items

# _* !!!
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record



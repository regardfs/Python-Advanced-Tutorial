# For python3 env

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, month, day) = data

############################################################
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

############################################################
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

############################################################
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
fields #['*', '-2', '-2', 'Unprivileged User']

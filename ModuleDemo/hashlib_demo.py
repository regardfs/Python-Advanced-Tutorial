import hashlib

# use md5 as the encryption algorithm
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()


# use sha1 as the encryption algorithm
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

# sometimes we use salt to enforce our password
salt = "123qax"


def get_password(username):
    pass


def login(username, password, the_salt):
    md5 = hashlib.md5()
    username = username
    input_password = md5.update(password + the_salt)
    user_password = get_password(username)
    if user_password == input_password:
        return 1
    else:
        return 0


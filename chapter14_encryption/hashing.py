import hashlib

md5 = hashlib.md5()
md5.update(b'Python rocks!')
print(md5.digest())

sha = hashlib.sha1(b'Hello Python').hexdigest()
print(sha)
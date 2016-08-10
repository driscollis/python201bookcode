import binascii
import hashlib

dk = hashlib.pbkdf2_hmac(hash_name='sha256',
                         password=b'bad_password34',
                         salt=b'bad_salt',
                         iterations=100000)
print(binascii.hexlify(dk))
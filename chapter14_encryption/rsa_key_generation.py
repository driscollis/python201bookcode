from Crypto.PublicKey import RSA

code = 'nooneknows'
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=code, pkcs=8,
                              protection="scryptAndAES128-CBC")

# Note - Be sure to change the path in the next two context managers to
# a valid path
with open('/path_to_private_key/my_private_rsa_key.bin', 'wb') as f:
    f.write(encrypted_key)

with open('/path_to_public_key/my_rsa_public.pem', 'wb') as f:
    f.write(key.publickey().exportKey())
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('/path/to/encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('/path_to_public_key/my_rsa_public.pem').read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)
import time
import string
import random

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
start_time = time.time()
class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = key
        
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        print(str(iv))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

if __name__ == "__main__":
    print(Random.new())
    secret_key = get_random_bytes(16)
    enc = AESCipher(secret_key)

    
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))

    encrypted_text = enc.encrypt(res)
    # print(encrypted_text)
    # print(enc.decrypt(encrypted_text))
    print("--- %s seconds ---" % (time.time() - start_time))
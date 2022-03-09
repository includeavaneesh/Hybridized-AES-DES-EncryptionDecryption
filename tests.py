import io
import time
import string
import random
import matplotlib.pyplot as plt

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
        
class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = key
        
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(encrypted_text).decode("utf-8")

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

class DESCipher(object):
    def __init__(self, key):
        self.block_size = DES.block_size
        self.key = key

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
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

    # Test 2: Image Analysis
    

    # Test 1: Encryption-Decryption Time Analysis
    datasize = []
    time_des = []
    time_aes = []
    i = 10
    m=0
    while i<=100000:
        
        print("----------------")
        m+=1
        i=i+1000
        datasize.append(m)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = i*8))
        
        start_time_DES = time.time()
        secret_key_DES = get_random_bytes(8)
        enc_DES = DESCipher(secret_key_DES)
        encrypted_text_DES = enc_DES.encrypt(res)
        enc_DES.decrypt(encrypted_text_DES)
        end_time_DES = time.time()
        # print("--- %s DES encryption time (seconds) ---" % (end_time_DES - start_time_DES))
        time_des.append(end_time_DES - start_time_DES)

        start_time_AES = time.time()
        secret_key_AES = get_random_bytes(16)
        enc_AES = AESCipher(secret_key_AES)
        encrypted_text_AES = enc_AES.encrypt(res)
        enc_AES.decrypt(encrypted_text_AES)
        end_time_AES = time.time()
        # print("--- %s AES encryption time (seconds) ---" % (end_time_AES - start_time_AES))
        time_aes.append(end_time_AES - start_time_AES)

    print(time_aes)
    print(time_des)
    print(datasize)

    plt.plot(datasize,time_aes,label = "AES")
    plt.plot(datasize,time_des,label = "DES")
    plt.xlabel("Size of Data ( Power of Mbit)")
    plt.ylabel("Time Taken to Encrypt and Decrypt")
    plt.legend()
    plt.show()
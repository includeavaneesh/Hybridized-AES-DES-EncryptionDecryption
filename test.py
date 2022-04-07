import AES_hybrid as aes_2
import time
import base64

# 1. Image Encryption

# with open("girl.jpg", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())

# start_time = time.time()
# encry=aes_2.encrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', my_string)
# print("time for encryption --- %s seconds ---" % (time.time() - start_time))
# # with open("encry_test_Img.txt", "wb") as img_file:
# #     img_file.write(encry)

# start_time2 = time.time()
# decry=aes_2.decrypt('ahdfsujeytsbsdfawskdfhsdgfereijd',encry)

# print("time for decryption --- %s seconds ---" % (time.time() - start_time2))
# with open("out_test_Img.jpg", "wb") as img_file:
#     img_file.write(base64.b64decode(decry))

#2. Text Encryption
BLOCK_SIZE = 16

def pad(plain_text):
    number_of_bytes_to_pad = BLOCK_SIZE - len(plain_text) % BLOCK_SIZE
    ascii_string = chr(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string
    padded_plain_text = plain_text + padding_str
    return padded_plain_text

def unpad(plain_text):
    last_character = plain_text[len(plain_text) - 1:]
    return plain_text[:-ord(last_character)]

my_string = 'avaneeshkanshi'
my_string = pad(my_string)
start_time = time.time()
encry=aes_2.encrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', my_string)
print("time for encryption --- %s seconds ---" % (time.time() - start_time))
with open("encry_test_Img.txt", "wb") as img_file:
    img_file.write(encry)

start_time2 = time.time()
decry=aes_2.decrypt('ahdfsujeytsbsdfawskdfhsdgfereijd',encry)
decry = unpad(decry)
print(decry.decode('utf-8'))

print("time for decryption --- %s seconds ---" % (time.time() - start_time2))


import random
import json
from sys import maxsize
from key_manager import write_key


class Encoder:
    def __init__(self, char_list):
        self.char_list = char_list
        random.shuffle(self.char_list)

    def encrypt(self, plain_text, file_name):
        enc_msg = ''
        shift = random.randint(5, maxsize)
        key = {" ": " "}

        for i in range(len(self.char_list)):
            key[self.char_list[i]] = self.char_list[(
                i + shift) % len(self.char_list)]

        for i in plain_text:
            if i in key:
                enc_msg += key[i]
            else:
                return "unrecognized character"

        write_key(file_name, key)

        return enc_msg  # returns tuple

    def decrypt(self, encrypted_text, key):
        dec_msg = ''
        file = key
        new_file = file[1:-1]
        file_list = new_file.split(sep="\\")
        file = '/'.join(file_list)

        json_dict = open(file, 'r', encoding='utf-8')
        key_dict = json.load(json_dict)

        reverse_key = {y: x for (x, y) in key_dict.items()}
        for i in encrypted_text:
            dec_msg += reverse_key[i]

        return dec_msg


# Usage example
# file = 'C:/Users/Timothy Chia/Desktop/Projects/Cipher/unicode basic latin.txt'
# char_list = open(file, 'r', encoding='utf-8')
# letters = []

# for i in char_list.read():
#     letters.append(i)

# char_list.close()

# encoder = Encoder(letters)
# msg = input('Enter message: ')
# enc_msg = encoder.encrypt(msg)
# print(f"Encrypted: {enc_msg[0]}")
# print(f"Shift: {enc_msg[1]}")
# print(f"Decrypted: {encoder.decrypt(enc_msg[0])}")

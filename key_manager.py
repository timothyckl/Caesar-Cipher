import json
from os import listdir

KEY_DIR = "PATH TO KEY DIRECTORY"


def write_key(file_name, key):

    def split(word):
        return [char for char in word]

    def create_json(file):
        dest_file = open(KEY_DIR + file, "w")
        json.dump(key, dest_file)

    file = f"{file_name}.json"
    key_dir_list = listdir(KEY_DIR)

    while True:
        if file in key_dir_list:
            print("\nFile name already exists. Choose another\n")
            new_file = input(">>> ")
            new_file = new_file + ".json"
            if new_file not in key_dir_list:
                create_json(new_file)
                break
        if file not in key_dir_list:
            create_json(file)
            break

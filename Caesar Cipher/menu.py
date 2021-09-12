from encoder import Encoder

file = 'unicode_basic_latin.txt' # You can replace the text file with whatever you want
char_list = open(file, 'r', encoding='utf-8')
letters = []

for i in char_list.read():
    letters.append(i)

char_list.close()

encoder = Encoder(letters)  # remember to add list


def menu():
    while True:
        print(f"\n{'='*40}")
        print("\tTrES Encryption Program")
        print(f"{'='*40}")
        print("\n1) Encrypt text")
        print("2) Decrypt text")
        print("0) Quit\n")
        choice = input(">>> ")
        try:
            choice = int(choice)
        except:
            print("Please enter a number.")
            continue

        if choice not in range(3):
            print("Out of range. Try again.")
            continue
        break
    return choice


while True:
    choice = menu()
    if choice == 1:
        try:
            msg = input("Enter text to be encrypted: ")
            key_name = input("Please name your key: ")
            enc_msg = encoder.encrypt(msg, key_name)

            if enc_msg == "unrecognized character":
                print("\nError. Unrecognised character.")
                input(f"\n{'-'*40}\nPress enter to continue...\n{'-'*40}")
            else:
                print(f"\nEncrypted text: {enc_msg}")
                input(f"\n{'-'*40}\nPress enter to continue...\n{'-'*40}")
        except Exception as error:
            print(f"Type of error: {error}")
            break
    elif choice == 2:
        try:
            msg = input("Enter text to be decrypted: ")
            key_location = input("Please enter your key: ")
            dec_msg = encoder.decrypt(msg, key_location)
            print(f"\nDecrypted text: {dec_msg}")
            input(f"\n{'-'*40}\nPress enter to continue...\n{'-'*40}")
        except Exception as error:
            print(f"Type of error: {error}")
    else:
        # quit()
        print("\nGoodbye!\n")
        break

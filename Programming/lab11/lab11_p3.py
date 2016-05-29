"""1. Reads messages in a tetxt file, and encodes the messages
    saved in a new file.
    2. For encoding a substitution key should be used
    3. Unencrypted message files have the extension txt
    4. Encrypted message files have the extension enc
    5. New key should be created everytime (file .key)
    6. Decrypt with a given file and a key """

import sys

def openFile(file_name):
    """Opens file and handles possible errors"""

    try:
        opened = open(file_name, 'r')
        return opened
    except:
        quit('Wrong file name... Please, try again.')


file_name = input('Enter a filename: ')
encrypt = False
decrypt = False

if (file_name.split('.'))[1] == 'txt':
    encrypt = True
else:
    decrypt = True

opened_file = openFile(file_name)

if encrypt:
    # Function for encryption
else:
    # Function for decryption

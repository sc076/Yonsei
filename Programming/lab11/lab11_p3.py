"""1. Reads messages in a tetxt file, and encodes the messages
    saved in a new file.
    2. For encoding a substitution key should be used
    3. Unencrypted message files have the extension txt
    4. Encrypted message files have the extension enc
    5. New key should be created everytime (file .key)
    6. Decrypt with a given file and a key """

import sys
import random
import copy

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def openFile(file_name):
    """Opens file and handles possible errors"""

    try:
        opened = open(file_name, 'r')
        return opened
    except:
        quit('Wrong file name... Please, try again.')

def generateKey(file_n):
    """ Function generating encryption key.
        In the format of dictionary with pairs:
        [real_value] -> encrypted_value
        Writes the key in file with extension key"""

    values = copy.deepcopy(alphabet)
    random.shuffle(values)

    code = {}

    # Generate random dictionary from alphabet structure
    for k in range(len(alphabet)):
        code[alphabet[k]] = values[k]

    # Constructs key file name
    file_name = file_n + '.key'

    # Save the dictionary values in a .key file
    code_file = open(file_name, 'w')
    for key in code:
        code_file.write(key + ',' + code[key] + '\n')

    # closes the file, returns the encryption code
    code_file.close()

    return code

def encrypt(o_file, file_name):
    """ Function implementing the encryption of the message """

    # gets the randomly generated key
    key = generateKey(file_name)

    # reads the message contained in the file
    content = o_file.read()
    o_file.close()

    # creating encrypted file
    encrypted = open(file_name + '.enc', 'w')

    # Starts encrypting
    for char in content:
        new_char = key.get(char)
        if new_char != None:
            encrypted.write(new_char)
        else:
            encrypted.write(char)
    encrypted.close

# --- MAIN
enc = False
dec = False

file_name = input('Enter a filename: ')

opened_file = openFile(file_name)
file_ext = file_name.split('.')[1]
file_n = file_name.split('.')[0]

if file_ext == 'txt':
    enc = True
else:
    dec = True

if enc == True:
    encrypt(opened_file, file_n)
elif dec == True:
    # Function for decryption
    print('Decrypt')

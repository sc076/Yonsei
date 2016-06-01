import sys
import random
import copy

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def openFile(file_name):
    """Opens file and handles possible errors"""

    try:
        opened = open(file_name, 'r')
        return opened
    except:
        quit('There was an error while opening the file.\nPlease, try again.')

def generateKey(file_n):
    """ Function generating encryption key.
        In the format of dictionary with pairs:
        [real_value] -> encrypted_value
        Writes the key in file with extension key"""

    values = copy.deepcopy(alphabet)
    random.shuffle(values)

    code = {}

    # Constructs key file name
    file_name = file_n + '.key'
    code_file = open(file_name, 'w')

    # Generate random dictionary from alphabet structure
    # and saves the pattern in a file
    for k in range(len(alphabet)):
        key = alphabet[k]
        val = values[k]
        code[key] = val
        code_file.write(key + ',' + val + '\n')

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
        if char.isupper():
            new_char = key.get(char)
            if new_char != None:
                encrypted.write(new_char)
            else:
                encrypted.write(char)
        else:
            new_char = key.get(char.upper())
            if new_char != None:
                encrypted.write(new_char.lower())
            else:
                encrypted.write(char)
    encrypted.close()

def getKey(file_name):
    """ Opens the file containing encrypting key and
        fills a dictionary with the values """

    # Opens and reads the key file
    key_file = open(file_name + '.key', 'r')
    key_dic = {}
    line = key_file.readline().strip('\n')

    while line:
        key_val = line.split(',')
        key_dic[key_val[1]] = key_val[0]
        line = key_file.readline().strip('\n')

    key_file.close()
    return key_dic

def decrypt(o_file, file_name):
    """ Function for used to decrypt the message
        First gets the encryption key then reads the
        message from the file and does the decryption
    """

    # Retrieves the decryption key
    key_dic = getKey(file_name)

    content = o_file.read()
    o_file.close()

    # Starts decryption
    decrypted = open(file_name + '.txt', 'w')

    for char in content:
        if char.isupper():
            new_char = key_dic.get(char)
            if new_char != None:
                decrypted.write(new_char)
            else:
                decrypted.write(char)
        else:
            new_char = key_dic.get(char.upper())
            if new_char != None:
                decrypted.write(new_char.lower())
            else:
                decrypted.write(char)
    decrypted.close()

# --- MAIN
file_name = input('Enter a filename: ')
try:
    file_ext = file_name.split('.')[1]
    file_n = file_name.split('.')[0]
except:
    quit('Wrong file. Try again.')

if file_ext == 'txt':
    opened_file = openFile(file_name)
    encrypt(opened_file, file_n)
elif file_ext == 'enc':
    opened_file = openFile(file_name)
    decrypt(opened_file, file_n)
else:
    print('Wrong file extension. Try again.')

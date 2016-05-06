#Palindrome Checker Program

def revrseStr(s):
    """ Function to reverse one half of
        the inputed string.
    """
    rvr = s[::-1]
    return rvr

#welcome message
print('This program can determine if a given string is a palindrome\n')
print('(Enter return to exit)')

#init
empty_string = ''

#get string from user
chars = input('Enter string to check: ')

while chars != empty_string:
    if len(chars) == 1:
        print('A one letter word is by definition a palindrom\n')
    else:
        #init
        is_palindrome = True
        reverse = revrseStr(chars)

        if reverse.lower() != chars.lower():
            is_palindrome = False

        #display results
        if is_palindrome:
            print(chars, 'is a palindrome\n')
        else:
            print(chars, 'is NOT a palindrome\n')

    #get next string from user
    chars = input('Enter string to check: ')

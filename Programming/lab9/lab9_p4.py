import re

def extractMessage(err_msg):
    """ Removes leading and trailing asterisks and blanks.

      extractMessage('** syntax error **') -> returns 'syntax error'
    """
    front = ''
    back = ''

    #Reads the front of the message until a symbol
    #different than asteriks or blank is met and keeps saves the order of chars
    for char in err_msg:
        if char != '*' and char != ' ':
            break
        front += char

    #removes the front of the string
    err_msg = err_msg.lstrip(front)

    #Does the same as above but for the back of the string
    #Uses reversed string
    revers = err_msg[::-1]
    for char in revers:
        if char != '*' and char != ' ':
            break
        back += char

    #Removes the back
    err_msg = revers.lstrip(back)

    #Returns the error message without front and back
    return err_msg[::-1]

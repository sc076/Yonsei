""" Polish notation type based calculator

"""
import stack
import sys

operand = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
operator = ('+', '-', '*','/')
flag = True

""" Helpper functions for the basic operations
    multiplication, add, substract, division.
    Contains also an error handling function,
    if the stack underflows, exits with error
    message.
"""
def multipl(a,b):
    return a*b

def division(b,a):
    return a/b

def plus(a,b):
    return a+b

def minus(b,a):
    return a-b
#Error handler function
def error():
    sys.exit('Not enough operands in expression')

def calculator(element, numbers):

    a = int(stack.pop(numbers)) if not stack.isEmpty(numbers) else error()
    b = int(stack.pop(numbers)) if not stack.isEmpty(numbers) else error()

    #Checks operator's type
    if element == '+':
        result = plus(a,b)
        stack.push(numbers, result)
    elif element == '-':
        result = minus(a,b)
        stack.push(numbers, result)
    elif element == '*':
        result = multipl(a,b)
        stack.push(numbers, result)
    elif element == '/':
        result = division(a,b)
        stack.push(numbers, result)


num = stack.getStack()

while flag == True:
    exp = input('Enter an RPN expression: ')
    for el in exp:
        if el in operand:
            stack.push(num, el)
        elif el in operator:
            calculator(el, num)
        elif el == '=':
            print('Value of expression: ', int(stack.pop(num)))
        else:
            flag = False
    #Resets the stack
    num = stack.getStack()

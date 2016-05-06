import stack

""" Ask the user to enter a series of braces and parentheses,
    then indicate if they are properly nested
"""

char = input('Enter parentheses and/or braces: ')

sequence = stack.getStack()

#for every element in the received string checks the type and pushes/pops in/from the stack
for el in char:
    if el == '(' or el == '{':
        stack.push(sequence, el)
    elif not stack.isEmpty(sequence):
        if el == ')' and stack.top(sequence) == '(':
            stack.pop(sequence)
        elif el == '}' and stack.top(sequence) == '{':
            stack.pop(sequence)

#Final check if the stack is empty
#If it's empty the string is proper
if stack.isEmpty(sequence):
    print('Nested properly.')
else:
    print('Not properly nested.')

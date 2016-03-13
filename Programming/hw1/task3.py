'''Write a program that outputs the last 4 digits of your student ID 
according to the digit maps on the next slide. Between each digit you 
should output one blank ' ' character'''

def printL():
# counter
    i = 0
    
    # outputs the first line
    while i < 3:
        print('*'*3, end=' ')
        i += 1

    print('*')
    i = 0

def printTF():
    print(' ', '*', end=' ' )
    i = 0
    while i<2:
        i+=1
        print('*'*3, end =' ')
    print('*')

def printT():
    i = 0
    print(' ', '*', end=' ')
    while i < 2:
        print('*', end =' '*3)
        i += 1
    i = 0
    print('*')

def printF():
    i = 0

    # line four
    while i < 3:
        i += 1
        print(' ', '*', end = ' ')

    print('*')
def print_id():
    printL()   
    printT()
    printTF()
    printF()
    printTF()
     
print_id()


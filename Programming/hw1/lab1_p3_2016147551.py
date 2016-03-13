#TASK3

'''Write a program that outputs the last 4 digits of your student ID 
according to the digit maps on the next slide. Between each digit you 
should output one blank ' ' character'''

#student ID = 7551

#Function which outputs first line of the digits
def printFirst():
    # counter
    i = 0
    # outputs the first line
    while i < 3:
        print('*'*3, end=' ')
        i += 1

    print('*')

#Outputs the second lije of the digits
def printSecond():
    i = 0
    print(' ', '*', end=' ')
    while i < 2:
        print('*', end =' '*3)
        i += 1
    i = 0
    print('*')

#Outputs the third and fifth line of the digits
def printTF():
    print(' ', '*', end=' ' )
    i = 0
    while i<2:
        i+=1
        print('*'*3, end =' ')
    print('*')


#Outputs third and fifts lines 
def printFourth():
    i = 0
    while i < 3:
        i += 1
        print(' ', '*', end = ' ')

    print('*')

printFirst()   
printSecond()
printTF()
printFourth()
printTF()


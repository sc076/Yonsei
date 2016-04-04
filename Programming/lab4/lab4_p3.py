# Prints a square of numbers from 1 to 100
'''
-----Version1------
for i in range(1, 101):
    print('%3d' %i, end=" ")
    if i%10 == 0:
        print()
'''

'''
----Downgrade Version 2 ------
while counter <=100:
    if counter%10 == 0:
        print('%3d' %counter)
    else:
        print('%3d' %counter, end=" ")
    counter += 1
'''
#----------- I reached the bottom ㅠㅠ Version 3 ------------
elem = 1
row = 0
while elem <= 100:
    while row < 10:
        print('%3d' %elem, end=" ")
        elem += 1
        row += 1
    print()
    row = 0
        

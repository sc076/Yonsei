# Program that asks for number and finds all the roots and powers of this number

num = int(input("Your number: "))

root = 1
flag = False

for pwr in range(2, 6):
    root = 1
    while (root**pwr) != num and root<num:
        root = root + 1
    if root**pwr == num: 
        flag = True
        print("root: " + str( root) + ", pwr:", pwr)
        root += 1
if flag == False:
    print('No matching pair of integers found')
    

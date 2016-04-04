num = int(input('Enter a number: '))

cpy_num = num 
counter = 0
while cpy_num != 0:
    counter += 1
    cpy_num = cpy_num//10

print('The number', num, 'contains', counter, 'digits') if counter > 1 \
        else print('The number', num, 'contains', counter, 'digit')


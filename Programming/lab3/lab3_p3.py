#Asks the user for ISBN number
isbn = input('Enter an ISBN:')

#Splits each group the ISBN by '-'
isbn_br = isbn.split('-')

#Outputs each group
print('{:.<20}'.format(isbn_br[0]) + 'GS1 prefix')
print('{:.<20}'.format(isbn_br[1]) + 'Group identifier')
print('{:.<20}'.format(isbn_br[2]) + 'Publisher code')
print('{:.<20}'.format(isbn_br[3]) + 'Item number')
print('{:.<20}'.format(isbn_br[4]) + 'Check digit')

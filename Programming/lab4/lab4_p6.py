#Reads the input from the user
income = int(input('Enter the taxable income in USD: '))

#Calculates the due depending on the amount
if income < 750:
    due = income*1/100
elif 750 <= income < 2250:
    due = 7.50 + (income - 750)*2/100
elif 2250 <= income < 3750:
    due = 37.50 + (income - 2250)*3/100
elif 3750 <= income < 5250:
    due = 82.50 + (income - 3750)*4/100
elif 5250 <= income < 7000:
    due = 142.50 + (income - 5250)*5/100
elif income >= 7000:
    due = 230 + (income - 7000)*6/100

#Outputs the due 
print('Tax due:',  '{0:.2f}'.format(due))

# User enter only positive integers
# 0 terminates the program and prints out the sum of the int

num = []

i = 1
while i != 0:
    i = int(input("Your number: "))
    num.append(i)

sm = 0

for i in num:
    if i<=100:
        sm += i

print("Sum:", sm)

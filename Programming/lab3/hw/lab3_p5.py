import random

lotto = []
for i in range(0, 6):
    lotto.append(random.randint(1, 45))

print('Lotto numbers of the week:', lotto[0], lotto[1], lotto[2], lotto[3], lotto[4], lotto[5], '\n')


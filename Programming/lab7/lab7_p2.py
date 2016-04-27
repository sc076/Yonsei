'''func modCount that is given positive int - n,
second positive int - m; m <= n
returns how many numbers between 1 to n are evenly
divisible by m
'''

def modCount(n, m):
    count = 0               #Counter for the divisors

    #Loops through the numbers in range [1, n]
    for i in range(1, n+1):
        if i%m==0:          #looks for a evenly divisible numbers
            count+=1

    #returns the result
    return count

#Write a function that evaluates the Polynomial
#3x^5+2x^4-5x^3-x^2+7x-6

#evaluating function
def evalPolynomial(x):
    result = 3*(x**5)+2*(x**4)-5*(x**3)-x**2+7*x-6 #calculates
    print("Polynomial for x="+str(x)+":", result)  #outputs the answer

#Main
val = int(input("Enter a value for x: "))
evalPolynomial(val)

'''Modify the Drake’s Equation Program in section 1.7 so that it calculates results for a best case scenario,

that is, so that factors p (percentage of stars that have planets), f (percentage of those planets that develop 

        life), i (percentage of those planets that develop intelligent life), and c (percentage of those planets that 

                can communicate with us) are all hard-coded as 100%. The value of R should remain as 7. Design the 

        program so that the only values that the user is prompted for are how many planets per star can support 

        life, n, and the estimated number of years civilizations last, L. Develop a set of test cases for your pro-
        gram with the included test results.
'''

#Variables and user input

R = 7  #Rate of star creation
p = 100 #Percentage of stars with planets
f = 100 #Percentage of planets that go on to intelligent devolep life
i = 100 #Percantage of planets thought to have inteligent life
c = 100 #Percantege of planets that can communicate with us
n = int(input('How many planets do you think actually develop life?: '))
L = int(input('Number of years you think civilizations last?: '))

#calculates result
num_detectable_civilizations = R*(p/100)*n*(f/100)*(i/100)*(c/100)*L

#display result
print('Based on the values entered ...')
print('there are an estimated', round(num_detectable_civilizations), 'potentially detectable civilizations in our galaxy')

1. a) Depends on the definition of few seconds and computer architecture.
   for around 5 seconds: it can execute 10^21 
   for around 1 second : it can execute 10^15 ~ 10^18
   
   b) There is no value X that the program will run forever.
	In order to run forever the statement in the while loop
	should be true for every iteration done by the while loop and the program should be unresponsive to the user.
	With the change of the variable ans in every iteration eventually the value of ans**3 will become bigger than abs(X)'s
	Rather the program can run for verry long time with big enough X, but still the statement will become False at some point.
   c)  Because in the while statement the program is taking the absolute value of X
 	for all numbers positive or negative integers the program will enter in infinite loop and the program will become unresponsive
	But for x = 0 the program will terminate outputing wanted answer because the statement ans**3 < abs(x) is False

2.	a), b), c)
3. 	a) 24 not in nums
	b) 'Ellen' in names
	c) v1)	print('Morris') if last_name == 'Morris' else print('Morrison')
	   v2)	if last_name == 'Morris':
			print('Morris')
		elif last_name == 'Morrison':
			print('Morrison')
	   v3)  if last_name < 'Morrison':
			print('Morris')
		else:
			print('Morrison')

4.	
4.1: There is error in identation levels 
4.2: The input the program is getting is of type str not int 
     -> The interpretator cannot multiply sequence by non-int
4.3: Product always will be 0
4.4: After fixing the above errors the product is not calculated properly
     The first entered value by the user is not included in the calculations
     After entering in the loop the user is asked to enter another value
			

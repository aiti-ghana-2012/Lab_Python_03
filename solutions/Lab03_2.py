"""
Lab_Python_03
Solutions for Question 2
"""

## Lab03_2a

print 'a:'

# 6 rows, starting with 1
for i in range(1,7):
	
	#in each row, we want to print as many numbers as
	#the row that we are on plust one
	for j in range(i):
		print j + 1,

	#and after each row, a newling
	print


## Lab03_2b
print #for space between problems
print 'b:'

#6 rows, starting with 0
for i in range(6):

	#in each row, we want to print as many numbers as
	#6 minus the row that we are on
	for j in range(6 - i):
		print j + 1,


	#and after each row, a newline
	print

## Lab03_2c
print
print 'c:'

#6 rows, starting with 1
for i in range(1,7):

	#in each row, we want to print 2 times 6 minus i spaces,
	#and then as many numbers as the row we are on, counting down
	print ' ' * 2 *(6 - i), #you can multiply strings!
	for j in range(i,0,-1):
		print j,

	#and then a newline
	print

## Lab04_2d
print
print 'd:'

#6 rows, starting with 0
for i in range(6):
	
	#in each row, we want to print (i) * 2 spaces,
	# and then count up to 6 minus i
	print ' ' * 2 * i,
	for j in range(6 - i):
		print j + 1,

	#and then a newline
	print


## Lab04_2e
print
print 'e:'

#5 rows, starting with 0
for i in range(5):
	
	#the strategy for is is a little different
	#we need to build a string for each row, and then print
	#it, to avoid the spaces that 'print j,' would output
	
	#so create a variable that will hold the row value
	row = ''
	
	#we start with (4 - i) spaces
	row += ' ' * (4 - i)
	
	#then we count down from (i + 1) to 1 (exclusive of 1)
	for j in range(i+1,1,-1):
		row += str(j) #important to use str() to turn j into a string

	#now we need to count up from 1 to i + 1 (inclusive of i+1)
	for j in range(1,i+2): #i + 2 in order to include i + 1
		row += str(j)

	#and finally print the row, without a ',' so that a newline is automatically printed
	print row

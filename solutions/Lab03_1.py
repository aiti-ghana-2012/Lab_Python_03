"""
Lab_Python_03
Solution for Question 1
"""

#program to get the first 50 primes

#print the first 50 primes
n = 50

print "the first 50 primes:"

#initialize the counter that keeps
#track of how many primes we have found
prime_count = 0

#possible_prime is the number that
#we are going to check to see if it's prime
#2 is the first prime number, so we start there
possible_prime = 2

#we want to keep looking for primes as long
#as we have found less than the number for which
#we are looking (which is 50 in this case)
while prime_count < n:

    #initialize a counter that will keep track of
    #the number of divisors that possible_prime will have
    divisor_count = 0

    #we want to loop over every number from
    #1 to possible_prime, checking if it is
    #a divisor of possible_prime
    for i in range(1,possible_prime+1):

        #if i is a divisor of possible_prime...
        if possible_prime % i == 0:
            #increment the divisor count by 1
            divisor_count += 1

    #now we check if possible_prime is actually a
    #prime by checking the number of divisors that it has
    #a prime number has exactly 2 divisors
    if divisor_count == 2:
        #if possible_prime is actually prime,
        #we want to print it WITHOUT a newline
        #(which is what the comma does - prevent the newline)
        print possible_prime,

        #we also have to increment the counter that
        #is keeping track of the number of primes
        #that we have seen.
        prime_count += 1

        #if the number of primes that we have seen is a
        #multiple of 10 (10,20,30,40,50...)
        #then we want to print a newline!
        if prime_count % 10 == 0:
            #'print' on a line alone will print just
            #a newline
            print

    #now we have to consider the next number to
    #be a possible prime
    possible_prime += 1



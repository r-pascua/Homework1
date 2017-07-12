# Robert Pascua
# Astronomy 9
# Homework 1
# Problem 3: Sieve of Eratosthenes
#
# The purpose of this program is to compute the sum of all primes
# less than some natural number N. The program first prompts the
# user to choose N and generates a list of all primes less than N
# using the Sieve of Eratosthenes algorithm. The program then
# computes the sum of the list elements and outputs the result.
# For testing convenience, the program asks the user if the
# program should be terminated or accept another number.

import math as m

# Initialize variable for choosing whether to terminate program
keepGoing = True

# Define upper bound for summation
N = 2

# Function for continuation prompt
def continueLoop():
	answer = input('Would you like to keep going? y/n: ')
	if answer.lower() != 'y':
		return False
	else:
		return True

# Function for prompting the user to set N
# Include protocols for invalid input
def getNumber():
	try:
		N = int(input('Enter a natural number: '))
	except ValueError:
		print("That isn't a natural number. Please try again.")
		N = getNumber()
	else:
		if N <= 0:
			print("Please enter a positive integer.")
			N = getNumber()
			
	return N
		

# Sieve of Eratosthenes Algorithm
# Returns summation of primes less than user-defined N
# This implementation based on the pseudocode provided by
# the Wikipedia page for the Sieve of Eratosthenes. The
# summation is included since it is most convenient to do so.
def sieve(N=2):
	# Initialize sum as zero
	primes = []
	# Generate boolean array for all natural n < N
	primesProxy = [ False, False ]
	for i in range(2, N):
		primesProxy.append(True)
	for i in range(2, int(m.sqrt(N))+1):
		if primesProxy[i]:
			j = i**2
			while j < N:
				primesProxy[j] = False
				j += i
	for i in range(2, N):
		if primesProxy[i]:
			primes.append(i)	
	sum = 0
	for i in range(len(primes)):
		sum += primes[i]
	return sum
	
while keepGoing:
	N = getNumber()
	result = sieve(N)
	print('The sum of all primes less than', N, 'is', str(result)+'.')
	keepGoing = continueLoop()
#Sabrina Reyes
'''
(10 points) Define a custom error class named ’EmptySet’ in Python3. And design a
function to perform cartesian product of two sets. If at least one the sets given to the
function, is an empty set then raise that error, and give some information to the user
and continue until two proper sets are given, after successfully computing the cartesian
product; print the result.
'''
class EmptySet(Exception):
	pass

#the assumption is that a user has to continuously add input until both sets are complete

def cartproduct():
	flag = 0
	while flag == 0:
		try:
			first_input = input('Type your first set here: ').split()
			first_Set = set(first_input)

			second_input = input('Type your second set here: ').split()
			second_Set = set(second_input)

			if second_Set == set() or first_Set == set():
				raise EmptySet

			a, b = len(first_Set), len(second_Set)

			print("The cartesian product is: ")
			for i in first_Set:
				for j in second_Set:
					print("{",i ,", ",j,"}", sep="",end="")
			flag = -1
		except EmptySet:
			print("One or two sets are empty. Please try again.")

cartproduct()
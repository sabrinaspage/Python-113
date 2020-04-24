from math import sqrt

#Name: Sabrina
#Assignment: Exercise 3
#CSC 11300-2L

#1
def is_perf():
	try:
		sum = 0
		check = int(input("To discover if a number is perfect, enter a number. <Negative to exit> >> "))
		while check >= 0:
			if check == 0:
				print("Because 0 is neither a natural number nor a positive integer, it is not a perfect number.")
				check = int(input("To try again, enter a number. <Negative to exit> >> "))
			for i in range(1, check): #start at 1 b/c otherwise zero mod
				if (check)%i == 0:
					sum = sum + i
			#print("The sum is", sum)
			if sum == check:
				print("Indeed,", check, "is a perfect number.")
			else:
				print("Sorry", check, "is not a perfect number.")
			sum = 0;
			check = int(input("To try again, enter a number. <Negative to exit> >> "))
	except ValueError as excObj:
		if str(excObj) == "math domain error":
			print("This should not happen.")
		else:
			print("Invalid input given.")
	except:
		print("Sorry. Something went wrong somewhere.")
is_perf()

#2
def all_positive_int():
	X = int(input("Enter a positive integer divisor. <Negative to exit> >> "))
	while X > 0:
		for i in range (1, X+1): #include X itself
			if X%i == 0:
				print(i, end = " ")
		X = int(input("\nEnter a positive integer divisor. <Negative or 0 to exit> >> "))
all_positive_int()

#3

def triangle():
	try:
		print("Welcome to triangle tracker. We will be tracking if the following points make a triangle using the triangle rule.")
		flag = "y"
		while flag[0] == "y" or flag[0] == "Y":
			X1, Y1 = [int(x) for x in input("Enter two coordinates here: ").split()] #I hope this is acceptable
			X2, Y2 = [int(x) for x in input("Enter two coordinates here: ").split()] #the hope is to take two integer values
			X3, Y3 = [int(x) for x in input("Enter two coordinates here: ").split()] #and split them into their respective areas

			dist1 = sqrt((X1-X2)**2 + (Y1-Y2)**2)
			dist2 = sqrt((X2-X3)**2 + (Y2-Y3)**2)
			dist3 = sqrt((X3-X1)**2 + (Y3-Y1)**2)

			if(dist1 + dist2 > dist3 and dist2 + dist3 > dist1 and dist1 + dist3 > dist2):
				print("This is a triangle.")
				flag = input("How about another time? <y or Y to continue> >> ")
			else:
				print("This is not a triangle.")
				flag = input("Would you like to try again? <y or Y to continue> >> ")
	except ValueError as excObj:
		print("Invalid coefficient given.")
	except:
		print("Goodbye.")
triangle()

#4
def prime_numbers():
	print("Welcome to the prime number finder. We will be finding the prime numbers between two integer numbers.")
	try:
		flag = "y" #first flag
		while flag[0] == "y" or flag[0] == "Y":
			x = int(input("Please enter the first integer: "))
			y = int(input("Please enter the second integer: "))
			if(x > y):
				temp = y
				y = x
				x = temp
			print("The prime numbers between ", x, " and ", y, " are: ")
			for i in range(x, y+1):
				if i >= 2:
					prime = 1 #flag to see if value is still prime outside of for loop
					for j in range(2, i):
						if i%j == 0: #so if i is 10, and j is 2, that gives 5, remainder 0; therefore it's not prime
							prime = 0;
							break;
					if prime == 1: #but if it's 11, and j never has a proper integer for it, then we're fine
						print(i, end = " ")
			flag = input("\nWould you like to try again? <y or Y to continue> >> ")
	except ValueError as excObj:
		print("Invalid coefficient given.")
	except:
		print("Goodbye.")
prime_numbers()

#5
def fact(x):
	fact = 1
	for i in range(2, x+1):
		fact *= i #i*i*i...a
	return fact

def permutation(x, y):
	return int(fact(x)/fact(x-y)) #permutation

def people_in_table():
	print("This program is used to discover the different ways y people of x in total can be seated in a table.")
	try:
		flag = "y"
		while flag[0] == "y" or flag[0] == "Y":
			x = int(input("Enter total number of people: "))
			y = int(input("Enter number of people to be seated: "))
			if y > x:
				print("Error. We cannot sit more people than there are.")
				flag = input("Would you like to to try again? <y or Y to continue> >> ")
			else:
				print("There are ", permutation(x, y), " ways to seat ", y, " people.")
				flag = input("Would you like to to try again? <y or Y to continue> >> ")
	except ValueError as excObj:
		print("Invalid coefficient given.")
	except:
		print("Goodbye.")
people_in_table()
#Sabrina Reyes
'''
Suppose you are given 2 lists of user defined size n, named Table1, Table2.
Make a Python3 program to distribute random probability values to the table cells. The
sum of each table entries must be 1 (k=1 for Table1, k=1 for Table2).
'''
import math
import random

n = int(input("What length would you like your tables to be? >> "))

Table1 = []*n
Table2 = []*n

def random_probability(table):
	#table = [random.randrange(1,n+1,1) for _ in range(n)]
	#fill the list with random values from 1 to n+1, 0 to n
	for i in range (1,n+1):
		table.append(random.randrange(1,n+1,1))
	#now take the sum of the table
	s = sum(table)
	#then divide each value of the table by the s
	#so each value is a probability of s
	table = [i/s for i in table]
	#return the table for use
	return table
print("The sume of each table is equal to 1.")
print(random_probability(Table1))
print(random_probability(Table2))
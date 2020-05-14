#Sabrina Reyes
#Assignment 3
#Question 4
'''
Create a 3D list in Python3 with random values [0-1000](size user
defined ‘n x n x n’, hence a cube). Then based on the dimensions of
the 3D list, create m number of randomly generated 2D lists of
indexes [0 - (n-1)]. Write a Python3 function to take the projection
of the 3D list onto m 2D lists that you randomly created. Your
program must return the elements of the 3D list projected onto the
indexes that 2D lists contain.

(Think of a cube, and a piece of paper which could be at most the
size of a side of the cube, (could be smaller), if the piece of paper
is sized exactly the same as the side of the cube, then the
projection is the piece of paper itself)
'''

import random

#if a list is 5 x 3 x 2, then there are 2 groups with three groups each with five groups each
flag = "y"
n = input("Enter the value for the dimensions of the cube:\n")
n = int(n)

#instead of creating for loops and appending each line
#use three for loops in a single array
def Cube(dimension):
	lst = [[ [random.randint(0,1000) for col in range(dimension)] for col in range(dimension)] for row in range(dimension)]
	return lst;
#pprint is just used to print the list
Full_Cube = Cube(n) #should store the values of said list
print("The 3d list is:\n",Full_Cube,"\n")

#create a list of all the sublists that will be projected onto it
sublists = []

#the 3d list will be transcribed in m 2d lists based on m = n-1 moves
for layer in Full_Cube: #first row
	for el in layer: #each element of first row
		sublists.append(el) #append the element for each of that row
print("The 3d list projected onto 2d sublists:\n", sublists,"\n")

#this prints the elements of 3d onto 2d list
def printproject(your_twod_list):
	print("The elements of the 3D list projected onto the 2D list:\n")
	for x in your_twod_list:
		print(*x, "\t", sep=' ')

printproject(sublists)
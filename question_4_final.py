#Sabrina Reyes
'''
(10 points) Let A be a ’matrix’ in Python containing randomly assigned values, belongs
to custom created matrix class, an instance of customly designed class named ’matrix’.
Write a Python3 program to rotate A clockwise (the 1st column becomes the 1st row)
n times and prints it to the screen.
If n = 4 then the result is the initial matrix A, if a negative number given for n then
rotate the matrix counterclockwise.
'''

import random

#let's choose four

class matrix(object):
	def __init__(self, rows, cols):
		self.matrix, self.rows, self.cols = [], rows, cols

		#initialize matrix rows with empty values
		for i in range(rows):
			self.matrix.append([])

		#now for every col per row, append a random value
		for j in self.matrix:
			for i in range(cols):
				j.append(random.randint(0, 100))

	def __repr__(self):
		for i in self.matrix:
			print('\t'.join(map(str,i)))

	def rotateclockwise(self):
	    temp_cols, temp_rows = self.rows, self.cols

	    # initialize the temp matrix
	    temp = []
	    for i in range(temp_rows):
	        temp.append([None for _ in range(temp_cols)])

	    # paste values into the temp matrix
	    for i in range(self.rows): #go through original array's rows
	        for j in range(self.cols): #go through originala array's columns
	            #whatever isn't new_i is new_j
	            temp_i = j #the new column consists of j values
	            temp_j = temp_cols - i - 1 #new row consists of the following value
	            temp[temp_i][temp_j] = self.matrix[i][j] #now set the temp array to the matrix' element

	    # print it out
	    #idk why __repr__ doesn't work here tho
	    return temp

	def rotatecounter(self):
		#must be negative for counter clockwise rotation
		temp_cols, temp_rows = self.rows, self.cols

	    # initialize the temp matrix
		temp = []
		for i in range(temp_rows):
		    temp.append([None for _ in range(temp_cols)])

		# paste values into the temp matrix
		for i in range(self.rows):
		    for j in range(self.cols):
		    	temp_i = temp_cols - j - 1
		    	temp_j = i
		    	temp[temp_i][temp_j] = self.matrix[i][j] #now set the temp array to the matrix' element

		return temp

	def k_rotate(self, k):
		if k%4 == 0:
			return self.matrix
		if k < 0:
			for i in range(k, 0, 1):
				self.matrix = self.rotatecounter()
			#set self.matrix to the matrix returned here
			return self.matrix
		if k > 0:
			for i in range(0, k):
				self.matrix = self.rotateclockwise()
			return self.matrix
			#set self.matrix to the matrix returned here

print("Initialize matrix and print.")
A = matrix(5,5)
A.__repr__()

n = 3
print("Rotate the ORIGINAL matrix",n,"times clockwise.")
B = A.k_rotate(n)
for i in B:
	print('\t'.join(map(str,i)))

n = -1
print("Rotate the PREVIOUS rotation",n,"times counter clockwise.")
C = A.k_rotate(n)
for i in C:
	print('\t'.join(map(str,i)))

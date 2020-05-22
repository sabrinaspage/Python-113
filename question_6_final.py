#Sabrina Reyes
'''
(10 points) Let A be a 2D list in Python containing randomly assigned values where its
size is also randomly generated up to 10 rows and 10 columns. Let B be another 2D list
in Python containing randomly assigned values where its size is also randomly generated
up to 10 rows and 10 columns. Write a Python3 program to check if we can multiply
these two lists as matrices (We are checking matrix multiplication rule).
'''

import random

rows1, rows2 = random.randint(1,10), random.randint(1,10)
cols1, cols2 = random.randint(1,10), random.randint(1,10)

A = []
for i in range(cols1):
	col = []
	for j in range(rows1):
		col.append(0)
	A.append(col)

for row in A:
	print(row)
print('\n')

B = []
for i in range(cols2):
	col = []
	for j in range(rows2):
		col.append(0)
	B.append(col)

for row in B:
	print(row)
print('\n')

def matrix_mult_chk(matrix1, matrix2):
	print("Matrix Multiplication Check")
	m1_rows, m1_cols = len(matrix1), len(matrix1[0])
	m2_rows, m2_cols = len(matrix2), len(matrix2[0])

	if((m1_rows == m2_cols) and (m1_cols == m2_rows)):
		#the number of columns of first matrix must equal number of rows in second
		#the number of rows of the first matrix must equal the number of cols in second
		return True
	return False
print("Matrix A and B can do matrix multiplication:", matrix_mult_chk(A, B))

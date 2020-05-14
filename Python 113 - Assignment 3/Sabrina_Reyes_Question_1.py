#Sabrina Reyes
#Assignment 3
#Question 1:
''' 
Let a .txt file contain n=1000 lines. In this file each line finishes
either with an ‘X’ or with a ‘Y’.
Design a function that randomly adds either ‘X’ or ‘Y’ to the end of
each line. Write the result back to the same file(do not append).
Then write another function to show the number of the lines finishing
with XX and YY and the ratio of the lines finishing with ‘XX’ and
‘YY’ / all n lines. (divide number of lines finishing with double X +
double Y by the total number of the lines)
'''
import random

fn = open('demo.txt', 'w')
#every other line has an X, else Y, in file fn
for i in range(1000):
	xvar = 'X'
	yvar = 'Y'
	array = ["this is line %d X\n" % i, "this is line %d Y\n" % i]
	fn.write(random.choice(array))
fn.close()

#random addition of X or Y to the end of each line
#each line was created anew and then written into a new file
#rather than appended
def randaddition():
	xvar = 'X'
	yvar = 'Y'
	newline=""
	with open('demo.txt', 'r') as f:
		for line in f:
			#result = random.choice([xvar, yvar])
			newline+=line.strip() + random.choice([xvar, yvar]) + "\n"
		f.close() #don't let it close within the for loop!!!
	with open('demo.txt', 'w') as f:
			f.write(newline)
			f.close()
randaddition()

def numoflines():
	countXX = 0 #how many XX?
	countYY = 0 #how many YY?
	n = 0 #how many lines are we at?
	with open('demo.txt', 'r') as f:
		if n < 1001:
			for line in f:
				n+=1
				if 'XX' in line:
					countXX += 1
				if 'YY' in line:
					countYY += 1
	f.close()
	#print(countXX, countYY, n)
	ratioXX = countXX/n
	ratioYY = countYY/n
	resultXXYY = ratioXX + ratioYY
	print("Ratio (XX:YY) " + str(countXX) + ":" + str(countYY))
	print("XX + YY ratio: " + str(resultXXYY))
numoflines()
#Sabrina Reyes
'''
(10 points) Make a user interface to get 3 points from the user which will be placed
on the coordinate plane. Then write a Python3 function to check whether the points
entered forms a right triangle. And another Python3 function to check whether the
points entered forms a equilateral triangle. Call your functions for three user-entered
points on the coordinate plane.
'''

from math import sqrt

class plot:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		print('The coordinates for this point are x: {}\n, y: {}\n, and z: {}\n'.\
			format(self.x, self.y))

print("Please enter the following coordinates: ")

plot1 = plot(
	float(input('x1: ')),
	float(input('y1: ')),
	#int(input('z1: '))
)

plot2 = plot(
	float(input('x2: ')),
	float(input('y2: ')),
	#int(input('z2: '))
)

plot3 = plot(
	float(input('x3: ')),
	float(input('y3: ')),
	#int(input('z3: '))
)

def distance(point1, point2, point3):
	distance_one = sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)
	distance_two = sqrt((point1.x-point3.x)**2 + (point1.y-point3.y)**2)
	distance_three = sqrt((point2.x-point3.x)**2 + (point2.y-point3.y)**2)
	return distance_one, distance_two, distance_three

def rightTriangle(point1, point2, point3):
	#BC = AC
	#BC^2+AC^2=AB^2
	#
	distance_one, distance_two, distance_three = distance(point1, point2, point3)
	print("Distances:", distance_one, distance_two, distance_three)
	#if the two sides = the hypotenuse
	if(distance_one**2 + distance_two**2 == distance_three**2):
		return True
	elif(distance_one**2 + distance_three**2 == distance_two**2):
		return True
	elif(distance_two**2 + distance_three**2 == distance_one**2):
		return True
	return False

print("The vertices entered create a right triangle:", rightTriangle(plot1, plot2, plot3))

def equilatriangle(point1, point2, point3):
	distance_one, distance_two, distance_three = distance(point1, point2, point3)
	print("Distances:", distance_one, distance_two, distance_three)
	
	if(distance_one == distance_two == distance_three):
		return True
	return False

print("The vertices entered comprise of an equilateral triangle:", equilatriangle(plot1, plot2, plot3))

#degenerate triangles exist btw so thats why plot1 === plot2 == plot3 is ok
#i can't find any coordinates that are good examples for this tho?!
#(0,0) (0,0) and (0,0) work tho
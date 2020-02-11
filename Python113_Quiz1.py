#Name: Sabrina Reyes
#Lab session: 2L, morning

import math

# Write a function to convert minutes to milliseconds. /
# Call your function for some example argument
def min_to_ms(min):
     millisec = min * 6000
     print(millisec);
min_to_ms(60)

# Use the math module import to use square root and compute the roots of a quadratic /
# equation. Call your function for the coefficients /
# a, b, c as 1, 2, 1 respectively.

def quad_eq(a, b, c):
    delta = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/2*a
    print ("Quadratic equation with plus is:", x1)
    print ("Quadratic equation with minus is:", x2)

quad_eq(1, 2, 1)

# Say you have a cube with side of n. /
# And you have some amount of marbles /
# (round, sphere) with radius n/4 ⁄ 
# How many marbles can you fit in the cube? Obtain the solution /
# with the use of functions. (Write a function and call it.)

def marbles_in_cube(n):
    r = n / 4
    marble_volume = (4/3)*math.pi*(r**3)
    cube_volume = n * n * n
    amount = cube_volume / marble_volume
    print("The number of marbles that can fit within the cube is", round(amount)) # either round or floor it

marbles_in_cube(8)

# Write a function and call the function to give the following output: (PS: \n, \t, if-else, and
# loops are not allowed)

def sill():
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^_ ^^")
def frame():
    print("i     i     i     i     i     i")
    print("i     i     i     i     i     i")
    print("i     i     i     i     i     i")
    print("i     i     i     i     i     i")
def window():
    sill()
    frame()
window()
window()
window()
window()
window()
window()
window()
sill()
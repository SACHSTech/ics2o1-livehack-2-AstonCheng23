"""
Name: Problem 2
Date: Febuary 23, 2021
Author: Aston
"""
print("----------RightTriangleMachine----------\n")

print("This program calculates if a triangle is a right triangle.")

#These are the side inputs.
a = float(input("Enter in a value for side 1: "))
b = float(input("Enter in a value for side 2: "))
c = float(input("Enter in a value for side 3: "))

#checks for the sides.
if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or c**2 + a**2 == b**2:
  print("It is a right triangle.")
else:
  print("It is not a right triangle.")
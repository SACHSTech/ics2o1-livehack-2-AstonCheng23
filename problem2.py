"""
Name: Problem 2
Date: Febuary 23, 2021
Author: Aston
"""
print("----------RightTriangleMachine----------\n")

print("This program calculates if a triangle is a right triangle.")

#These are the side inputs.
side_1 = float(input("Enter in a value for side 1: "))
side_2 = float(input("Enter in a value for side 2: "))
side_3 = float(input("Enter in a value for side 3: "))

#checks for the sides.
if side_1**2 + side_2**2 == side_3**2 or side_3**2 + side_2**2 == side_1**2 or side_3**2 + side_1**2 == side_2**2:
  print("It is a right triangle.")
else:
  print("It is not a right triangle.")
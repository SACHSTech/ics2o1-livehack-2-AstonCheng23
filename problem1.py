"""
Name: Problem 1
Date: Febuary 23, 2021
Author: Aston
"""

print("----------SpeedLimitRadar----------\n")

#these ask for your speed and the speed limit.
speed_limit = float(input("What is the speed limit?\n: "))
speed = float(input("How fast are you going?\n: "))

#checks for speed and if you should be fined.
if speed <= speed_limit + 20 and speed > speed_limit:
  print("You are speeding " + str(speed - speed_limit) + " kilometers above the speed limit. Your fine is $100 dollars.")
elif speed <= speed_limit + 30 and speed > speed_limit + 20:
  print("You are speeding " + str(speed - speed_limit) + " kilometers above the speed limit. Your fine is $270 dollars.")
elif speed > speed_limit + 30:
  print("You are speeding " + str(speed - speed_limit) + " kilometers above the speed limit. Your fine is $570 dollars.")
elif speed <= speed_limit:
  print("Congratulations, you are not speeding.")
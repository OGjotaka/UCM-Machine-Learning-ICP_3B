#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 8

'''
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
“The area of a circle with radius 10 is 314 meters square.”
'''

# initalize radius and area calculation
radius = 10
area = 3.14 * radius ** 2

# Using an f-string for easier and more readable formatting
result = f"The area of a circle with radius {radius} is {int(area)} meters square."
print(result)

# recieve radius as input from user
radius = float(input("Enter the radius of the circle: "))

# Using an f-string for easier and more readable formatting
area = 3.14 * radius ** 2
result = f"The area of a circle with radius {radius} is {int(area)} meters square."
print(result)

#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 5

import math


'''
The radius of a circle is 30 meters.
• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
• Calculate the circumference of a circle and assign the value to a variable name of
_circum_of_circle_
• Take radius as user input and calculate the area
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
# Create a circle object with a radius of 30 meters
circle = Circle(30)

# Access the radius attribute of the circle object
print("Radius of the circle:", circle.radius, "meters")

# Calculate the area of the circle
_area_of_circle_ = circle.calculate_area()
print("Area of the circle:", round(_area_of_circle_, 4), "square meters")

# Calculate the circumference using the formula
circumference = circle.calculate_circumference()
print("Circumference of the circle:", round(circumference, 4), "meters")

# Take radius input from the user
radius = float(input("Enter the radius of the circle: "))

# Update the radius of the circle object
circle.radius = radius

# Calculate the area using the formula
area = circle.calculate_area()
print("Area of the circle:", round(area, 4), "square meters")

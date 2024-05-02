#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 3

'''
• Create a tuple containing names of your sisters and your brothers (imaginary siblings are
fine)
• Join brothers and sisters tuples and assign it to siblings
• How many siblings do you have?
• Modify the siblings tuple and add the name of your father and mother and assign it to
family_members
'''
# Create a tuple containing names of sisters and brothers
siblings_tuple = ('Ashley', 'Daniel', 'Kevin', 'Emily', 'Ryan', 'Sophie')

# Print the tuple
print("Tuple containing names of sisters and brothers:", siblings_tuple)

# Tuples containing names of sisters and brothers
sisters_tuple = ('Ashley', 'Emily', 'Sophie')
brothers_tuple = ('Daniel', 'Kevin', 'Ryan')

# Join brothers and sisters tuples
siblings = sisters_tuple + brothers_tuple

# Print the resulting tuple
print("Joined tuple containing names of siblings:", siblings)

# Count siblings
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

# Define the parents tuple
parents = ('Pamela', 'Troy')

# Join siblings and parents tuples
family_members = siblings + parents

# Print the resulting tuple
print("Family members:", family_members)


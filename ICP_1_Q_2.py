#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 2

'''
Create an empty dictionary called dog
• Add name, color, breed, legs, age to the dog dictionary
• Create a student dictionary and add first_name, last_name, gender, age, marital status,
skills, country, city and address as keys for the dictionary
• Get the length of the student dictionary
• Get the value of skills and check the data type, it should be a list
• Modify the skills values by adding one or two skills
• Get the dictionary keys as a list
• Get the dictionary values as a list
'''

# create empty dictionary
dog = {}

# create keys and display
dog['name'] = " "
dog['color'] = " "
dog['breed'] = " "
dog['legs'] = " "
dog['age'] = " "
print(dog.keys())

# create student dict and add keys
student = {'first_name': ' ', 'last_name': ' ', 'gender': ' ', 'age': ' ', 'marital_status': ' ','skills': [], 'country': ' ', 'city': ' ', 'address': ' '}
print(student.keys())

# get length of student direcory
length_student_dict = len(student)
print("Length of Student", length_student_dict)

# Get value of skills and data type
skills_value = student['skills']
skills_data_type = type(skills_value)
print("Skills value:", skills_value)
print("Skills data type:", skills_data_type)


# add two skills and print
student['skills'].extend(['Computer_Science', 'Communication'])
print(skills_value)

# Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys as a list:", keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print("Values as a list:", values_list)


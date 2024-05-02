#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 9

'''
Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop. N: No of students (Read input from user)
Ex: L1: [150, 155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
'''

# ask user to list of weights
def get_weights_from_user():
    # Prompt the user to enter weights separated by commas
    input_string = input("Please enter a list of weights separated by commas: ")
    
    # Split the string into individual number strings based on commas
    weights_strings = input_string.split(',')
    
    # Convert the list of number strings to a list of integers
    weights_list = [int(num.strip()) for num in weights_strings]
    
    return weights_list

# Calling the function and storing the weights in a list
user_entered_weights = get_weights_from_user()

# Print the list of numbers to verify
print("You entered the following weights:", user_entered_weights)

# count the number of weights in the list
weights_count = len( user_entered_weights)
print("N = ", weights_count)

# Convert to kilos in separate list
weights_in_kilos = [weight / 2.2046 for weight in user_entered_weights]

# Print each weight in kilos
print("Weights in kilos:")
for weight, kilo in zip(user_entered_weights, weights_in_kilos):
    print(f"{weight} lbs = {kilo:.2f} kg")

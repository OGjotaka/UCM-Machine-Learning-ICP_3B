#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 4

'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
• Find the length of the set it_companies
• Add 'Twitter' to it_companies
• Insert multiple IT companies at once to the set it_companies
• Remove one of the companies from the set it_companies
• What is the difference between remove and discard
• Join A and B
• Find A intersection B
• Is A subset of B
• Are A and B disjoint sets
• Join A with B and B with A
• What is the symmetric difference between A and B
• Delete the sets completely
• Convert the ages to a set and compare the length of the list and the set.
'''

# create sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# get length of it-compaies direcory
length_company_dict = len(it_companies)
print("Length of Company Directory: ", length_company_dict)

# add to company
it_companies.add('Twitter')
print(it_companies)

print(it_companies)

# add multiple to it_companies
it_companies.update(['Meta', 'Samsung', 'Intel'])
print(it_companies)

# I just want to point out that it's weird how it puts these in... like  in what order are you yeeting shit into this list
# like I get that in Python - sets are unordered pairs
# but the two print statements back-to-back would have producded different results if there wasn't SOME internal stucture
# is there a seed value that Python uses as a language that would lead to this?
# It feels really familiar like the rondomization problem in C

# remove an element
it_companies.remove('Facebook')
print(it_companies)

'''
Both methods will remove the specified element from the set if it exists. However, if you use the remove()
method and the element does not exist in the set, it will raise a KeyError exception. On the other hand, the
discard() method will not raise an exception if the element does not exist in the set; it will simply do nothing.
'''

# join A and B - use | operator
print("A = ", A)
print("B = ", B)
result_set = A | B
print(result_set)

# find intersection of A & B using the & operator
intersection_set = A & B
print("Intersection of A & B: ", intersection_set)

# is A subset of B
is_subset = A <= B
print("A is subset of B: ", is_subset)

# is B subset of A
is_subset = B <= A
print("B is subset of A: ", is_subset)

# are A and B disjointed sets
are_disjoint = not A.intersection(B)
print("A and B are digjoint sets: :", are_disjoint)

# join A with B and B with A
result_set_1 = A | B
result_set_2 = B | B
print(result_set_1)
print(result_set_2)

# what is the symmetric difference between A and B
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)

# delete the sets completely
del A
del B

# convert the ages to a set and compare the length of the list and the set
# Convert the list to a set
print("Age List = ", age)
age_set = set(age)
print("Age Set:", age_set)

# Compare the lengths of the list and the set
if len(age) == len(age_set):
    print("The length of the list and the set are the same.")
else:
    print("The length of the list and the set are different.")
    age = [20, 25, 30, 20, 35, 25, 40]

# Convert the list to a list that includes duplicates
age_with_duplicates = list(age)

# Print the list with duplicates
print("Age with duplicates: ", age_with_duplicates)

# Convert the list to a list that includes duplicates
age_with_duplicates = list(age)


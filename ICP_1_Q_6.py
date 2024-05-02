#CS 4710
#JJ Holbrook
#700514202
#ICP 1 Question 6

'''
“I am a teacher and I love to inspire and teach people”
• How many unique words have been used in the sentence? Use the split methods and set
to get the unique words.
'''

# read a sentence from the user
sentence = input("Enter a sentence: ")

# split the sentence into words
words = sentence.split()

# create a set from these words
words_set = set(words)

# print the set to see the unique words
print(len(words_set))
print("The unique words in the sentence are:", words_set)

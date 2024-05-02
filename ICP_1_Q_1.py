#CS 4710
#JJ Holbrook
#700514202
#Question 1

'''
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
• Sort the list and find the min and max age
• Add the min age and the max age again to the list
• Find the median age (one middle item or two middle items divided by two)
• Find the average age (sum of all items divided by their number)
• Find the range of the ages (max minus min)
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sort ages ascending and display
ages.sort()
print(ages)

#find min and max and display
print("Minimum = ", min(ages))
print("Maximum = ", max(ages))

# addn min and max age to the list again
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# find the median
ages.sort()
mid = len(ages) // 2
res = (ages[mid] + ages[~mid]) / 2
print("Median = ", str(res))

# fnd the average
average = sum(ages) / len(ages)
print("Average = ", average)

# find the range
print("Range = ", max(ages) - min(ages))

#CS 4710
#JJ Holbrook
#700514202
#ICP 3 Part B Question 1-9

'''
1. Read the provided CSV file ‘data.csv’.
2. Show the basic statistical description about the data.
3. Check if the data has null values.
a. Replace the null values with the mean
4. Select at least two columns and aggregate the data using: min, max, count, mean.
5. Filter the dataframe to select the rows with calories values between 500 and 1000.
6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
8. Delete the “Maxpulse” column from the main df dataframe
9. Convert the datatype of Calories column to int datatype.
'''
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Print the DataFrame
#print(df)

# Show basic statistical description
description = df.describe()
print(description)

# Check for null values
null_values = df.isnull().any()

# Display the result
print("Null values in the DataFrame:")
print(null_values)

# Replace null values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Display the DataFrame after replacing null values
print(df)

# Select the columns and aggregate the data
aggregated_data = df[['Pulse', 'Maxpulse']].agg(['min', 'max', 'count', 'mean'])

# Display the aggregated data
print(aggregated_data)

# Filter the DataFrame for Calories between 500 and 1000
filtered_df = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

# Display the filtered DataFrame
print(filtered_df)

# Filter the DataFrame for Calories > 500 and pulse < 100
filtered_df = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# Display the filtered DataFrame
print(filtered_df)

# Create a new DataFrame df_modified without the "Maxpulse" column
df_modified = df.drop(columns=['Maxpulse'])

# Display the modified DataFrame
print(df_modified)

# Delete the "Maxpulse" column from the main DataFrame df
df.drop(columns=['Maxpulse'], inplace=True)

# Display the modified DataFrame
print(df)

# Convert the datatype of the "Calories" column to integer
df['Calories'] = df['Calories'].astype(int)

# Display the DataFrame with the modified datatype
print(df)

"""Create a food dictionary from a csv file
Created by Janna Lei Eugenio
22/06/2021 - version 1
"""

import csv

# open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# read dara from above into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary = {}

# add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

"""Takes external csv and converts amount in ml to g
Created by Janna Lei Eugenio
22/06/2021 - version 2
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


complete_list = False
while not complete_list:
    amount = eval(input("How much? "))

    # get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    if ingredient in food_dictionary:
        factor = food_dictionary.get(ingredient)
        amount = amount * float(factor) / 250
        print("Amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    another_item = input("\nPress 'enter' to add another item\n"
                        "Enter any key to end: ")
    if not another_item:
        continue
    else:
        complete_list = True

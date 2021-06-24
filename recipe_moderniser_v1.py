"""Recipe moderniser - full working program
Gets recipe name and recipe source (components 1 & 2)
Version 1 - includes 'To Do' list
Created by Janna Lei Eugenio
23/06/2021
"""

# Modules to be used
import csv

# FUNCTIONS
# Function to get recipe name and check it contains no digits
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        ask_again = input(question)

        if not num_ok:
            for letter in ask_again:  # Check for digits
                if letter.isdigit():  # Tests for true
                    number = True

        if not ask_again or number is True:  # generate error for blank name or digits
            print(error)

        else: # no error found
            return ask_again

# MAIN ROUTINE

# set up dictionaries

# set up list to hold 'modernised' ingredients

# get recipe name and check its not blank and contains no numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank, or contain numbers!",
                        False)   # False to disallow digits

# get recipe source and check it's not blank (numbers ok)
recipe_source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank!",
                   True)    # True to allow digits

# get serving sizes and desired number of servings

# get ingredients
# loop for each ingredient:
# get ingredient amount
# scale amount using scale factor
# get ingredient name and check it's not blank and doesn't contain numbers
# get unit
# convert to ml
# convert from ml to g
# add updated ingredient to list

# output modernised recipe
print("The recipe is for {}".format(recipe_name))
print("The recipe is from {}".format(recipe_source))

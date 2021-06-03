"""Get recipe name from user, checking that it does not contain any numbers and
is not left blank
Created by Janna Lei Eugenio
version 1 - 3/06/2021
"""

# get recipe name
recipe = input("What is the recipe name? ")

# check each character is in the recipe name and find any numbers
contains_number = False
for letter in recipe:
    if letter.isdigit():
        contains_number = True

# Print error message if recipe is blank or has numbers
if not recipe or contains_number:
    print("ERROR - input is blank ot has numbers in it")
else:
    print("We are making {}".format(recipe))

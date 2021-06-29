"""Recipe moderniser - full working program
Incorporates ingredient list splitter (component 9)
Created by Janna Lei Eugenio
29/06/2021 - version 4
"""

# Modules to be used
import csv
import re


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

        else:  # no error found
            return ask_again


# number checker
def check_num(question):
    while True:
        try:
            ask = float(input(question))
            if ask <= 0:
                print("Please enter a number greater than 0")
            else:
                return ask
        except ValueError:
            print("Please enter a number")


def get_scale_factor():
    run = True
    while run is True:
        # get serving size
        recipe_serving = check_num("How many servings does the recipe make? ")
        # Get desired number of servings
        desired_serving = check_num("Servings needed? ")
        # Calculate scale factor
        scale_factor = desired_serving / recipe_serving
        if scale_factor < .25:
            print("\nScale factor: {}".format(scale_factor))
            print("WARNING: This scale factor is very small and you might struggle"
                  "\nto accurately weigh the ingredients. Please consider using a"
                  "\nlarger scale factor and freezing the leftovers")
            change_scale_factor = ""
            while change_scale_factor != "y" or change_scale_factor != "n":
                change_scale_factor = input("\nWould you like to change it? (y/n) "
                                            ).lower()
                if change_scale_factor == "y":
                    break
                elif change_scale_factor == "n":
                    run = False
                    break
                print("Please input 'y' or 'n'")
        elif scale_factor > 4:
            print("\nScale factor: {}".format(scale_factor))
            print("Warning: This scale factor is quite large so you might have "
                  "\nissues with mixing bowl volumes and oven space. Please "
                  "\nconsider using a smaller scale factor and making more than "
                  "one batch.")
            change_scale_factor = ""
            while change_scale_factor != "y" or change_scale_factor != "n":
                change_scale_factor = input("\nWould you like to change it? (y/n) "
                                            ).lower()
                if change_scale_factor == "y":
                    break
                elif change_scale_factor == "n":
                    run = False
                    break
                print("Please input 'y' or 'n'")
        else:
            break
    return scale_factor


# Function to get and check amount, unit and ingredient
def get_all_ingredients():
    ingredient_list = []  # Set up ingredient list
    valid = False
    print("\nEnter ingredient on one line - qty, unit, then name ('X' to exit):")
    line_number = 1
    while not valid:
        ingredient = not_blank("{}: ".format(line_number), "Ingredient cannot be blank!",
                               True).title()
        if ingredient != "X":  # Check for exit code X
            ingredient_list.append(ingredient)  # Add ingredient to list
            line_number += 1
        else:
            if len(ingredient_list) < 2:  # Check that list has at least two items
                print("Please enter at least two ingredients")
            else:
                valid = True  # If list contains at least 2 items break out of loop
                return ingredient_list


# MAIN ROUTINE

# set up dictionaries

# set up list to hold 'modernised' ingredients
modernised_recipe = []

# get recipe name and check its not blank and contains no numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank, or contain numbers!",
                        False)  # False to disallow digits

# get recipe source and check it's not blank (numbers ok)
recipe_source = not_blank("Where is the recipe from? ",
                          "The recipe source can't be blank!",
                          True)  # True to allow digits

# get serving sizes and desired number of servings
# Calculate scale factor
scale_factor = get_scale_factor()

# get ingredients
full_recipe = get_all_ingredients()

# split ingredient into amount, unit and ingredient
mixed_regex = r"\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d - digit, /d{1,3} - allows 1-3 digits, /s - space, \/ - divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # testing to see if recipe line matches regular expression
    if re.match(mixed_regex, recipe_line):
        # get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # replace the space in mixed number with '+'
        amount = mixed_num.replace(" ", "+")

        # changes the string into a float and scales quantity
        amount = eval(amount) * scale_factor

        # get unit and ingredient
        compile_regex = re.compile(mixed_regex)  # compile into string

        unit_ingredient = re.split(compile_regex, recipe_line)

        unit_ingredient = (unit_ingredient[1]).strip()
        # removes extra white space before and after unit
        # 2nd element convert to string

    else:
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # convert amount to float
            amount = amount * scale_factor
        except NameError:
            amount = get_amount[0]

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)  # splits string into list

    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        unit = get_unit[0]
        ingredient = get_unit[1]
        modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))
    else:
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))


# convert to ml
# convert from ml to g
# add updated ingredient to list

# output modernised recipe
# print("\nThe recipe is for {}".format(recipe_name))
# print("The recipe is from {}".format(recipe_source))
for item in modernised_recipe:
    print(item)

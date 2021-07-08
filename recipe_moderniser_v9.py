"""Recipe moderniser - full working program
Changes to formatting - variable names and line lengths - to meet PEP8
Created by Janna Lei Eugenio
8/07/2021 - version 9
"""

# Modules to be used
import csv
import re


# FUNCTIONS
# function to round numbers appropriately
def round_amount(amount_to_round):
    if amount_to_round % 1 == 0:
        amount_to_round = int(amount_to_round)
    elif amount_to_round * 10 % 1 == 0:
        amount_to_round = "{:.1f}".format(amount_to_round)
    else:
        amount_to_round = "{:.2f}".format(amount_to_round)

    return amount_to_round


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

        if not ask_again or number is True:  # generate error for blank name
            print(error)  # or digits

        else:  # no error found
            return ask_again


# number checker
def check_num(question):
    error = "Please enter a number greater than 0"
    while True:
        response = input(question)
        try:
            response = eval(response)
            response = float(response)
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)
        except NameError:
            print(error)
        except SyntaxError:
            print(error)


def get_scale_factor():
    run = True
    # get serving size
    recipe_serving = check_num("\nWhat is the recipe serving size?"
                               "(Enter 1 if unsure): ")
    # Get desired number of servings
    desired_serving = check_num("How many servings are needed?"
                                "(Enter 1 if unsure): ")
    # Calculate scale factor
    factor = desired_serving / recipe_serving

    while run is True:
        if factor < .25:
            print("\nScale factor: {}".format(factor))
            print("WARNING: This scale factor is very small and you might \n"
                  "struggle to accurately weigh the ingredients. Please \n"
                  "consider using a larger scale factor and freezing \n"
                  "the leftovers")
            change_scale_factor = ""
            while change_scale_factor != "y" or change_scale_factor != "n":
                change_scale_factor = input("\nWould you like to change it? "
                                            "(y/n) ").lower()
                if change_scale_factor == "y":
                    factor = get_scale_factor()
                    break
                elif change_scale_factor == "n":
                    run = False
                    break
                print("Please input 'y' or 'n'")
        elif factor > 4:
            print("\nScale factor: {}".format(factor))
            print("Warning: This scale factor is quite large so you might have"
                  "\nissues with mixing bowl volumes and oven space. Please "
                  "\nconsider using a smaller scale factor and making more"
                  "\nthan one batch.")
            change_scale_factor = ""
            while change_scale_factor != "y" or change_scale_factor != "n":
                change_scale_factor = input("\nWould you like to change it? "
                                            "(y/n): ").lower()
                if change_scale_factor == "y":
                    factor = get_scale_factor()
                    break
                elif change_scale_factor == "n":
                    run = False
                    break
                else:
                    print("Please input 'y' or 'n'")
        else:
            break
    return factor


# Function to get and check amount, unit and ingredient
def get_all_ingredients():
    ingredient_list = []  # Set up ingredient list
    valid = False
    print("\nEnter ingredient on one line - qty, unit, then name "
          "('X' to exit):")
    line_number = 1
    while not valid:
        ingredient_name = not_blank("{}: ".format(line_number),
                                    "Ingredient cannot be blank!",
                                    True).lower()
        if ingredient_name != "x":  # Check for exit code X
            ingredient_list.append(ingredient)  # Add ingredient to list
            line_number += 1
        else:
            if len(ingredient_list) < 2:  # Check that list has at least
                print("Please enter at least two ingredients")  # two items
            else:
                return ingredient_list


def general_converter(amount2, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount2 *= float(factor) / conversion_factor
        converted = True
    else:
        converted = False

    return [amount2, converted]


def unit_checker(raw_unit):
    # ask user for unit
    unit_to_check = raw_unit

    # abbreviation list
    teaspoon = ["teaspoon", "tsp", "t", "teaspoons"]
    tablespoon = ["tablespoon", "tbsp", "tbs", "T", "tablespoons"]
    ounce = ["fluid ounce", "oz", "fl oz", "ounce", "ounces", "oz."]
    cup = ["cup", "c", "cups"]
    pint = ["pint", "p", "pt", "fl pt", "pints"]
    quart = ["quart", "q", "qt", "fl qt", "quarts"]
    ml = ["milliliter", "millilitre", "cc", "ml", "mls", "milliliters",
          "millilitres", "mL", "mLs"]
    litre = ["liter", "litre", "L", "liters", "litres"]
    decilitre = ["deciliter", "decilitre", "dL", "dl", "deciliters",
                 "decilitres", "dls", "dLs"]
    pound = ["pound", "lb", "lbs", "#", "pounds", "lb.", "lbs."]
    grams = ["g", "gram", "gms", "grams", "gms"]

    if not unit_to_check:
        return unit_to_check

    elif unit_to_check in teaspoon:
        return "teaspoon"
    elif unit_to_check in tablespoon:
        return "tablespoon"
    elif unit_to_check in ounce:
        return "ounce"
    elif unit_to_check in cup:
        return "cup"
    elif unit_to_check in pint:
        return "pint"
    elif unit_to_check in quart:
        return "quart"
    elif unit_to_check in ml:
        return "ml"
    elif unit_to_check in litre:
        return "litre"
    elif unit_to_check in decilitre:
        return "decilitre"
    elif unit_to_check in pound:
        return "pound"
    elif unit_to_check in grams:
        return "gm"
    else:
        return unit_to_check  # if unit is not in the list


# Instructions for first time users - optional
def instructions():
    print()
    print("******** INSTRUCTIONS ********")
    print()
    print("This program converts recipe ingredients to mls / grams and also"
          "allows\nusers to up-size or down-size ingredients.")
    print()
    print("The program also asks for the number of servings. If you are not \n"
          "sure, type '1'. Then when it asks for servings needed, you can \n"
          "increase\nor decrease the amount (e.g. 2 or 1/2) and the program \n"
          "will scale the ingredient amounts for you.")
    print()
    print("Note that you can use fractions if needed. For example, write\n"
          "one half as 1/2 and one and 3 quarters as 1 3/4")
    print()
    print("Please only type in one ingredient per line, if a recipe says\n"
          "'butter or margarine', choose ONE ingredeint, either butter\n"
          "or margarine")
    print()
    print("Lastly, all lines should start with a number / fraction unless\n"
          "no number is given (e.g. a pinch of salt)")
    print()
    print("******************************")
    print()


# MAIN ROUTINE

# set up dictionaries
unit_dict = {
    "teaspoon": 5,
    "tablespoon": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "decilitre": 100,
    "ml": 1,
    "gm": 1
}

# To check for errors in numeric entry of quantity
problem = False

# set up dictionary of conversion factors for ingredients
# open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# read dara from above into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dict = {}

# add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_groceries:
    food_dict[row[0]] = row[1]

# set up list to hold 'modernised' ingredients
modernised_recipe = []

# Providing option for new user to get instructions
print("******** Welcome to the Great Recipe Moderniser ********")
print()

get_instructions = input("Press <enter> to get instructions, or any\n"
                         "other key if you have used this program before: ")
if not get_instructions:
    instructions()
else:
    print()

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
            modernised_recipe.append(recipe_line)
        except SyntaxError:
            problem = True
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)  # splits string into list

    # Count the number of spaces in the recipe line
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        if unit == "gm":
            modernised_recipe.append("{:.0f} gm {}".format(amount, ingredient))
            continue

        amount = general_converter(amount, unit, unit_dict, 1)

        if amount[1]:
            amount_2 = general_converter(amount[0], ingredient, food_dict, 250)
            if amount_2[1]:
                modernised_recipe.append("{:.0f} gm {}".format(amount_2[0],
                                                               ingredient))
            else:
                modernised_recipe.append("{:.0f} ml {}".format(amount[0],
                                                               ingredient))

        else:
            amount[0] = round_amount(amount[0])
            modernised_recipe.append("{} {} {}".format(amount[0], unit,
                                                       ingredient))

    else:
        amount = round_amount(amount)
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))

# Output details of recipe
print("\n************{}************".format(recipe_name))
print("Source: {}\n".format(recipe_source))
print("***** Ingredients - scaled by a factor of {} *****\n"
      .format(scale_factor))

if problem:
    print("***** WARNING *****")
    print("Some of the entries bellow might be incorrect as there were some\n"
          "problems processing some of your inputs. It's possible that you\n"
          "typed a fraction incompletely.\n")

# output modernised recipe
for item in modernised_recipe:
    print(item)

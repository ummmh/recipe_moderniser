"""Second version of a combined converter using a function
Converts amount to mls and (if possible) converts mls to g
Created by Janna Lei Eugenio
30/06/2021 - version 2
"""
import csv


def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= float(factor) / conversion_factor
        converted = "yes"
    else:
        converted = "no"

    return [amount, converted]


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # ask user for unit
    unit_to_check = input("Unit? ")

    # abbreviation list
    teaspoon = ["teaspoon", "tsp", "t", "teaspoons"]
    tablespoon = ["tablespoon", "tbsp", "tbs", "T", "tablespoons"]
    ounce = ["fluid ounce", "oz", "fl oz", "ounce", "ounces"]
    cup = ["cup", "c", "cups"]
    pint = ["pint", "p", "pt", "fl pt", "pints"]
    quart = ["quart", "q", "qt", "fl qt", "quarts"]
    ml = ["milliliter", "millilitre", "cc", "ml", "mls", "milliliters",
          "millilitres", "mL", "mLs"]
    litre = ["liter", "litre", "L", "liters","litres"]
    decilitre = ["deciliter", "decilitre", "dL", "dl", "deciliters", "decilitres",
                 "dls", "dLs"]
    pound = ["pound", "lb", "lbs", "#", "pounds"]

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
    else:
        return unit_to_check   # if unit is not in the list


# main routine
# set up dictionary
unit_dict = {
    "teaspoon": 5,
    "tablespoon": 15,
    "cup": 250,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "decilitre": 100,
    "ml": 1
}

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

# Get items
complete_list = False
while not complete_list:
    # ask user for amount
    amount = eval(input("How much? "))

    # get unit and change to match dictionary
    unit = unit_checker()

    # check if unit in dictionary
    ingredient = input("Ingredient: ").lower()

    # convert to ml if possible
    amount = general_converter(amount, unit, unit_dict, 1)

    # If converted to mls, try to convert grams
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dict, 250)
        if amount_2[1] == "yes":
            print(round(amount_2[0],1), "grams")
        else:
            print(round(amount[0],1), "mls (ingredient not in conversion"
                                       " dictionary)")
    else:
        print(round(amount[0],1), unit, "(unable to convert to grams)")

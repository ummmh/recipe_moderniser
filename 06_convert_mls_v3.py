"""Get amount and unit from user then check if unit is in dictionary of units
If it is, convert to mls, otherwise leave as is
version 3 - builds on v2 referencing abbreviations of units to dictionary
Created by Janna Lei Eugenio
21/06/2021
"""

# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # ask user for unit
    unit_to_check = input("Unit? ")

    # abbreviation list
    teaspoon = ["teaspoon", "tsp","t"]
    tablespoon = ["tablespoon", "tbsp", "tbs", "T"]
    ounce = ["fluid ounce", "oz", "fl oz"]
    cup = ["cup", "c"]
    pint = ["pint", "p", "pt", "fl pt"]
    quart = ["quart", "q", "qt", "fl qt"]
    ml = ["milliliter", "millilitre", "cc", "mL"]
    litre = ["liter", "litre", "L"]
    decilitre = ["deciliter", "decilitre", "dL"]
    pound = ["pound", "lb", "lbs", "#"]

    if not unit_to_check:
        print("You chose no unit")
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
        return "mL"
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
    "decilitre": 100
}


complete_list = False
while not complete_list:
    # ask user for amount
    amount = eval(input("How much? "))

    # get unit and change to match dictionary
    unit = unit_checker()

    # check if the unit is in the dictionary
    if unit in unit_dict:                # if unit in dictionary convert to ml
        factor = unit_dict.get(unit)
        amount *= factor
        print("amount in ml {}".format(amount))
    else:                                # if unit unknown, leave as is
        print("{} is unchanged".format(amount))

    # to end the loop of items to check
    another_item = input("\nPress 'enter' to add another item\n"
                         "Enter any key to end: ")
    if not another_item:
        continue
    else:
        complete_list = True

"""Further version of an ingredient splitter which splits the ingredients from
one line of input into quantity, unit, and ingredient
Created by Janna Lei Eugenio
24/06/2021 - version 3 - testing full recipe
"""

import re # regular expression module

# Reading from a full list of Singredients
# ingredient has mixed fractions followed by unit and ingredient
full_recipe = [
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1 3/4 cups flour",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
]

# expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d - digit, /d{1,3} - allows 1-3 digits, /s - space, \/ - divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # testing to see if recipe line matches regular expression
    if re.match(mixed_regex, recipe_line):
        # get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # replace the space in mixed number with '+'
        amount = mixed_num.replace(" ","+")

        # changes the string into a float
        amount = eval(amount)

        # get unit and ingredient
        compile_regex = re.compile(mixed_regex)    # compile into string

        unit_ingredient = re.split(compile_regex, recipe_line)

        unit_ingredient = (unit_ingredient [1]).strip()
        # removes extra white space before and after unit
        # 2nd element convert to string

    else:
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # convert amount to float
        except NameError:
            amount = get_amount[0]

        unit_ingredient = get_amount[1]


    get_unit = unit_ingredient.split(" ", 1)
    # splits string into list
    unit = get_unit[0]
    ingredient = get_unit[1]

    # All 3 elements
    print("{} {} {}".format(amount, unit, ingredient))

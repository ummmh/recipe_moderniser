"""Further version of an ingredient splitter which splits the ingredients from
one line of input into quantity, unit, and ingredient
Created by Janna Lei Eugenio
24/06/2021 - version 2
"""

import re # regular expression module

# ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour"  # change to input statement in due course

# expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d - digit, /d{1,3} - allows 1-3 digits, /s - space, \/ - divide

# testing to see if recipe line matches regular expression
if re.match(mixed_regex, recipe_line):
    print("True")
    # get mixed number by matching the regex
    pre_mixed_num = re.match(mixed_regex, recipe_line)
    mixed_num = pre_mixed_num.group()

    # replace the space in mixed number with '+'
    amount = mixed_num.replace(" ","+")

    # changes the string into a float
    amount = eval(amount)
    print(amount)

    # get unit and ingredient
    compile_regex = re.compile(mixed_regex)    # compile into string
    print(compile_regex)

    unit_ingredient = re.split(compile_regex, recipe_line)
    print(unit_ingredient)

    unit_ingredient = (unit_ingredient [1]).strip()
    # removes extra white space before and after unit
    # 2nd element convert to string
    print(unit_ingredient)

get_unit = unit_ingredient.split(" ", 1)
# splits string into list
print(get_unit)
unit = get_unit[0]
ingredient = get_unit[1]

# All 3 elements
print(amount)
print(unit)
print(ingredient)

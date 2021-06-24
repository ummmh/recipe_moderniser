"""Initial version of an ingredient splitter which splits the ingredients from
one line of input into quantity, unit, and ingredient
Created by Janna Lei Eugenio
24/06/2021 - version 1
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
else:
    print("False")

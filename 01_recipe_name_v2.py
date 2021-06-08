"""Get recipe name from user, checking that it does not contain any numbers and
is not left blank
Created by Janna Lei Eugenio
version 2 - 3/06/2021
"""


# Function to get recipe name and check it contains no digits
def not_blank(recipe):
    valid = False

    while not valid:
        number = False   # Initial assumption - name contains no digits
        ask_again = input(recipe)

        for letter in ask_again:    # Check for digits
            if letter.isdigit():    # Tests for true
                number = True

        if not ask_again or number == True:
            print("ERROR - input is blank or contains a number")

        else:
            valid = True
            return ask_again

# Main Routine
recipe_name = not_blank("What is the recipe name? ")
print("You are making {}".format(recipe_name))

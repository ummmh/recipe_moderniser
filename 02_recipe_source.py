"""Get recipe source from user, checking that input is not left blank and
allowing user to allow or disallow digits
Created by Janna Lei Eugenio
8/06/2021
"""


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


# Main Routine
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank!", True)
print("The recipe is from {}".format(source))

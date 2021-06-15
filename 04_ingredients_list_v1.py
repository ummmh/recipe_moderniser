"""Get the ingredients required to make recipe, adding them to a list and then
printing the list at the end
Created by Janna Lei Eugenio
15/06/2021
"""

# Add user for ingredient name
def not_blank(question):
    valid = False

    while not valid:
        ask = input(question)

        if not ask:       # Check that response has been enter
            # If no response, generate error message
            print("Please enter an ingredient name (cannot be blank)")

        else:             # No error found
            return ask

# Main routine
ingredient_list = []     # Set up ingredient list
valid = False
while not valid:
    ingredient = not_blank("Enter ingredient name ('X' to exit): ").title()
    if ingredient != "X":  # Check for exit code X
        ingredient_list.append(ingredient)    # Add ingredient to list
    else:
        if len(ingredient_list) < 2:  # Check that list has at least two items
            print("Please enter at least two ingredients")
        else:
            valid = True # If list contains at least 2 items break out of loop
            print("Here are your ingredients:\n{}".format(ingredient_list))
            # Print list


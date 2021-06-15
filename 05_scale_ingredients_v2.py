"""Evaluates fractions for scale factor, rounds scale amounts, and prevents
entry of digits in ingredient name
Created by Janna Lei Eugenio
16/06/2021 - version 2
"""

# number checker
def check_num(response):
    while True:
        try:
            if response <= 0:
                response = float(input("Please enter a number greater than 0: "
                                       ""))
            else:
                return response
        except ValueError:
            print("Please enter a number")

# Add user for ingredient name
def not_blank(question):
    valid = False

    while not valid:
        ask = input(question)

        if not ask:       # Check that response has been enter
            # If no response, generate error message
            print("Please enter an ingredient name (cannot be blank)")

        elif not ask.isalpha():  # Checks that ingredient name has no digits
            print("The ingredient name can't contain digits")

        else:             # No error found
            return ask


# Main routine
scale_factor = eval(input("Scale factor: "))      # replace with component 3
# eval allows scale to be in  (1/3)
ingredient_list = []     # Set up ingredient list
valid = False

while not valid:

    amount = input("input amount ('X' to exit): ")
    if amount.upper() != "X":
        if not amount or not amount.isdigit():  # don't allow blanks or strings
            print("Please enter a valid amount")
        else:
            amount = float(amount)  # converts amount into a float
            scaled = check_num(amount) * scale_factor

            # Remove decimal point for whole numbers
            if scaled % 1 == 0:
                scaled = int(scaled)
            elif scaled * 10 % 1 == 0:
                scaled = "{:.1f}".format(scaled)  # rounds to 1dp (1.50 to 1.5)
            else:
                scaled = "{:.2f}".format(scaled)  # 2dp

            ingredient = not_blank("Enter ingredient name: ").title()
            # Calls not blank function and provides question
            ingredient_list.append("{} units {}".format(scaled, ingredient))
            # adds both elements on the same line
    elif len(ingredient_list) >= 2:
        valid = True
        print("\nHere are your ingredients:")
        for item in ingredient_list:
            print(item)
    else:
        print("Please enter at least two ingredients")



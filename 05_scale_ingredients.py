"""Get the scale factor, then the ingredient and amount required for each then
add the ingredients with their scaled amounts into a list to be printed at the
end.
Created by Janna Lei Eugenio
16/06/2021
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

        else:             # No error found
            return ask

# Main routine
scale_factor = float(input("Scale factor: "))     # Replace with component 3
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



"""Ask user for number of servings in recipe and number of servings desired and
then calculate number of servings desired and then calculate the scale factor
Created by Janna Lei Eugenio
9/06/2021
"""

# number checker
def check_num(question):
    while True:
        try:
            ask = float(input(question))
            if ask <= 0:
                print("Please enter a number greater than 0")
            else:
                return ask
        except ValueError:
            print("Please enter a number")

# Main routine
run = True
while run is True:
    # get serving size
    recipe_serving = check_num("How many servings does the recipe make? ")
    # Get desired number of servings
    desired_serving = check_num("Servings needed? ")
    # Calculate scale factor
    scale_factor = desired_serving / recipe_serving
    if scale_factor < .25:
        print("\nScale factor: {}".format(scale_factor))
        print("WARNING: This scale factor is very small and you might struggle"
              "\nto accurately weigh the ingredients. Please consider using a"
              "\nlarger scale factor and freezing the leftovers")
        change_scale_factor = input("\nWould you like to change it? (y/n) "
                                        ).lower()
        if change_scale_factor == "n":
            break
    elif scale_factor > 4:
        print("\nScale factor: {}".format(scale_factor))
        print("Warning: This scale factor is quite large so you might have "
              "\nissues with mixing bowl volumes and oven space. Please "
              "\nconsider using a smaller scale factor and making more than "
              "one batch.")
        change_scale_factor = input("\nWould you like to change it? (y/n) "
                                    ).lower()
        if change_scale_factor == "n":
            break
    else:
        break

print("\nScale factor: {}".format(scale_factor))

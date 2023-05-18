# imports

# functions go here
# ask question and check if input is in list
def q_in_list(question, lists, error):
    # loop until valid answer
    valid = False
    while not valid:
        response = input(question).lower()
        for var_list in lists:
            if response in var_list:
                response = var_list[0].title()
                return response
        # if invalid display error
        else:
            print(error)


# function for checking numbers (num_check)
def num_check(num):
    # check if num is within range, 0 - 999
    try:
        if 0 < float(num) < 1000:
            # rounds to 3 decimal points
            num = round(float(num), 3)
            return num
    # if value error returns error
    except ValueError:
        return "Invalid"
    # if any other error, also returns invalid
    return "Invalid"

# function for string check (checking if person entered area or perimeter)

    # If triangle or parallelogram ask if they want area or perimeter or both
    # If triangle: input(do you want area / perimeter)string check

# function for checking how many inputs are needed
# Circle(1): radius(r)
# Square(2): side 1(x), side 2(y)
# Triangle(4): base(x), height(h), side 2(y), side 3(z)
# Parallelogram(3): base(x), length(y), height(h)

# Maybe do lists for each shape with each input
# For item in list
# input(list[0])


# function for inputting dimensions

# function for doing area and perimeter  calculations
# (store the formulas in a dictionary somewhere else make this function generic and reusable)
    # Area = calculator(x, y, h)
    # Perimeter = calculator(x, y, z)

# setting up dictionaries and lists
    # Different shape names dictionary
valid_shapes = [
    ["rectangle", "rec", "rec", "r"],
    ["triangle", "tri", "t"],
    ["parallelogram", "para", "parallel", "p"],
    ["circle", "cir", "c"],
    ["xxx"]
]

# List of formulas for each shape
# Keep lists for dimensions, (side 1=x, height=h, side 2=y, side 3=z, radius=r)


# Start loop
shape = ''
while shape != 'Xxx':
    # Instructions

    # Ask user what shape they would like to select
    shape = q_in_list("Select shape: ", valid_shapes, "Error - Please enter rectangle, circle, "
                                                      "triangle or parallelogram")
    # print shape for testing purposes
    print(shape)
# Area or perimeter( if applicable)

# Enter dimensions

# Calculations

# Add to list

# Display history

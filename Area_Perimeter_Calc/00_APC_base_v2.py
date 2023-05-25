# imports

# functions go here
# ask question and check if input is in list
def in_list(question, lists, error):
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


def dimension_q(subtractor, error):
    inputted_dimensions = dimensions.copy()
    # use dict to ask user for dimension input
    for i in range(len(shape_dimensions[shape]) + subtractor):
        validity = "Invalid"
        # checking if input is valid and numerical
        while validity == "Invalid":
            inputted_dimensions[i] = input(shape_dimensions[shape][i])
            validity = num_check(inputted_dimensions[i])
            if validity == "Invalid":
                print(error)
        # adding inputted dimensions to list
        history[i].append(inputted_dimensions[i])
    return history, inputted_dimensions


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

history = [
        [],
        [],
        [],
        []
    ]

# dictionary with shape as key, dimensions
shape_dimensions = {'Rectangle': ['height: ', 'base: '],
                    'Circle': ['radius: '],
                    'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
                    'Parallelogram': ['base: ', 'sides: ', 'height: ']}

dimensions = ['x', 'y', 'z', 'h']

# list for valid area/perimeter responses
valid_area_perimeter = [
    ['area', 'a'],
    ['perimeter', 'p', 'per']
]


# List of formulas for each shape
# Keep lists for dimensions, (side 1=x, height=h, side 2=y, side 3=z, radius=r)


# Start loop
shape = ''
while shape != 'Xxx':
    # Instructions

    # Ask user what shape they would like to select
    shape = in_list("Select shape: ", valid_shapes, "Error - Please enter rectangle, circle, "
                                                    "triangle or parallelogram")
    if shape == 'Triangle' or shape == 'Parallelogram':
        # check for correct area/perimeter input
        area_perimeter = in_list("Calculate area or perimeter?: ", valid_area_perimeter,
                                 "Error - Please enter either area or perimeter")
        # if they choose perimeter, it excludes the last input, height
        if area_perimeter == 'Perimeter':
            subtract = -1
        else:
            subtract = 0
    else:
        subtract = 0
    # add dimensions to list to display history at the end
    dimension_history = dimension_q(subtract, "Please enter a number between 0.1 and 999")
    x = len(shape_dimensions[shape]) + subtract
    for z in range(x, 4):
        history[x].append('0')
        x += 1
# Calculations

# Add to list

# Display history

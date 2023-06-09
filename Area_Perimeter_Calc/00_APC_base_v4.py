# imports
from sympy import symbols, pi


# functions
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


# asks user for dimensions according to shape entered
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
    return inputted_dimensions


# calculates area/perimeter. Substitutes dimensions into given formula
def calculations(formula, result, substitutions, placement):
    if area_perimeter == "Perimeter":
        product = formula.subs({x: substitutions[0], y: substitutions[1], z: substitutions[2]})
    else:
        product = formula.subs({x: substitutions[0], y: substitutions[1], z: substitutions[2],
                                h: substitutions[3]})
    product = round(product, 3)
    print(str(result) + str(product))
    history[placement].append(product)
    return product


# setting up dictionaries and lists
# shape names dictionary
valid_shapes = [
    ["rectangle", "rec", "rec", "r"],
    ["triangle", "tri", "t"],
    ["parallelogram", "para", "parallel", "p"],
    ["circle", "cir", "c"],
    ["xxx", "x"]
]

# dimension questions for each shape
shape_dimensions = {'Rectangle': ['height: ', 'base: '],
                    'Circle': ['radius: '],
                    'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
                    'Parallelogram': ['base: ', 'sides: ', 'height: ']}

# stating symbols for sympy equations
x, y, z, h = symbols("x, y, z, h")

# area formula's according to shape
area_formula = {'Rectangle': x * y,
                'Circle': float(pi) * x ** 2,
                'Triangle': (x * h)/2,
                'Parallelogram': z * x
                }

# perimeter formula's according to shape
perimeter_formula = {'Rectangle': 2 * x + 2 * y,
                     'Circle': 2 * float(pi) * x,
                     'Triangle':  x + y + z,
                     'Parallelogram': 2 * x + 2 * y
                     }

# template for dimensions inputted by user
dimensions = ['x', 'y', 'z', 'h']

# list for valid area/perimeter responses
valid_area_perimeter = [
    ['area', 'a'],
    ['perimeter', 'p', 'per']
]

# list to keep track of all dimensions and calculations
history = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

# Start loop
shape = ''
while shape != 'Xxx':
    # Instructions

    # Ask user what shape they would like to select
    shape = in_list("Select shape: ", valid_shapes, "Error - Please enter rectangle, circle, "
                                                    "triangle or parallelogram")
    if shape == "Xxx":
        break
    # if shape is triangle of parallelogram ask for area/perimeter
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
        area_perimeter = ''
        subtract = 0
    # asks user for the dimensions of their shape
    dimension_history = dimension_q(subtract, "Please enter a number between 0.1 and 999")
    # fills in the unused dimensions with 0
    a = len(shape_dimensions[shape]) + subtract
    for a in range(a, 4):
        history[a].append('0')
        a += 1
# does calculations with shape and dimensions, displays area and/or perimeter
    if area_perimeter == "Perimeter":
        perimeter = calculations(perimeter_formula[shape], "Perimeter: ", dimension_history, 5)
        history[4].append('n/a')
    elif area_perimeter == "Area":
        area = calculations(area_formula[shape], "Area: ", dimension_history, 4)
        history[5].append('n/a')
    else:
        area = calculations(area_formula[shape], "Area: ", dimension_history, 4)
        perimeter = calculations(perimeter_formula[shape], "Perimeter: ", dimension_history, 5)
    print()
# Display history

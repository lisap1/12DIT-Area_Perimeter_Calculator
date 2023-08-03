# imports
from sympy import symbols, pi
import pandas


# functions
# ask question and check if input is in list
def in_list(question, lists, error):
    # loop until input is in list
    valid = False
    while not valid:
        response = input(question).lower()
        # if input is valid, return response
        for var_list in lists:
            if response in var_list:
                response = var_list[0].title()
                return response
        # if invalid display error
        else:
            print(error)


# function for checking numbers, numerical and within range
def num_check(num):
    # allows exit code
    if num == 'xxx':
        return 'exit'
    # check if num is within range, 0.01 - 999
    try:
        if 0.01 <= float(num) < 1000:
            return True
    # if value error returns error
    except ValueError:
        return False
    # if any other error, also returns invalid
    return False


# asks user for dimensions according to shape entered
def dimension_q(subtractor, error):
    inputted_dimensions = dimensions.copy()
    # establishing ranges for asking dimensions
    if shape == "Triangle" and area_perimeter == "Area":
        b = list(range(0, 1)) + list(range(3, 4))
    elif shape == "Parallelogram" and area_perimeter == "Area":
        b = list(range(0, 1)) + list(range(2, 3))
    else:
        b = range(len(shape_dimensions[shape]) + subtractor)
    for i in b:
        # asking user for inputs, makes sure is valid
        valid = False
        while not valid:
            inputted_dimensions[i] = input(shape_dimensions[shape][i])
            valid = num_check(inputted_dimensions[i])
            if valid == 'exit':
                return 'xxx'
            if not valid:
                print(error)
        # if shape is parallelogram, reorders dimensions for data frame
        if shape == 'Parallelogram' and i == 2:
            history[4].append(inputted_dimensions[i])
        else:
            # adding inputted dimensions to list
            history[i + 1].append(inputted_dimensions[i])
    # returns valid list of dimensions
    return inputted_dimensions


# calculates area/perimeter. Substitutes dimensions into given formula
def calculations(formula, result, substitutions, history_placement, unit):
    if area_perimeter == "Perimeter":
        product = formula.subs({x: substitutions[0], y: substitutions[1], z: substitutions[2]})
    else:
        product = formula.subs({x: substitutions[0], y: substitutions[1], z: substitutions[2],
                                h: substitutions[3]})
    # adds unit of measurement to calculation
    if result == 'Area: ':
        unit = str(unit + '^2')
    product = round(product, 3)
    print(str(result) + str(product) + ' ' + str(unit))
    history[history_placement].append(product)
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
shape_dimensions = {'Rectangle': ['base: ', 'height: '],
                    'Circle': ['radius: '],
                    'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
                    'Parallelogram': ['base: ', 'sides: ', 'height: ']}

# stating symbols for sympy equations
x, y, z, h = symbols("x, y, z, h")

# area formula according to shape
area_formula = {'Rectangle': x * y,
                'Circle': float(pi) * x ** 2,
                'Triangle': (x * h)/2,
                'Parallelogram': z * x
                }

# perimeter formula according to shape
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
    ['perimeter', 'p', 'per'],
    ['xxx']
]

yes_no = [
    ['yes', 'y', 'ye'],
    ['no', 'n', 'xxx']
]

measurement_units = [
    ['cm', 'centimetres', 'centimetre', 'centimeter', 'centimeters'],
    ['m', 'metre', 'metres', 'meter', 'meters'],
    ['in', 'inches', 'i', 'inch'],
    ['km', 'kilometre', 'kilometres', 'kilometer', 'kilometers'],
    ['mi', 'miles', 'mile'],
    ['mm', 'millimetre', 'millimetres', 'millimeter', 'millimeters'],
    ['ft', 'feet', 'foot'],
    ['yd', 'yards', 'yard'],
    ['n', '', 'no', 'n', 'none', 'xxx']
]

# list to keep track of all dimensions and calculations
history = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

# pandas dictionary
history_dict = {
    'Shape': history[0],
    'Base/Radius': history[1],
    'Side 1': history[2],
    'Side 2': history[3],
    'Height': history[4],
    'Area': history[5],
    'Perimeter': history[6],
    'Unit': history[7]
}

# shape ascii for instructions
shape_ascii = {
    'Rectangle': " _________________\n"
                 "|                 |\n"
                 "|                 |  Height\n"
                 "|                 |\n"
                 " -----------------\n "
                 "       Base",
    'Triangle': "            / \\\n"
                "           / |  \\\n"
                "  Side 1  /  |    \\  Side 2\n"
                "         /   | Height\n"
                "        /    |        \\\n"
                "       /-----|----------\\\n"
                "             Base\n",
    'Parallelogram': "        _____________________\n"
                     "       / |                  /\n"
                     "      /  |  Height         / Sides\n"
                     "     /   |                /\n"
                     "    /----|---------------/\n"
                     "              Base",
    'Circle': "    __________\n"
              "  /            \\\n"
              "/        Radius  \\\n"
              "|       *------- |\n"
              " \\              /\n"
              "   \\ ________ /\n",
}

shape_count = 1

# check if the user wants instructions
display_instructions = in_list("Display instructions?(enter yes or no) : ", yes_no, "Error - Please enter yes or no")
print()
# Start loop
shape = ''
while shape != 'Xxx':
    # Instructions, selecting shape
    if display_instructions == "Yes":
        print("Select a shape by typing it after 'Select shape: '\n"
              "Select rectangle, circle, triangle or parallelogram\n"
              "Shortcut: first letter of shape, e.g. 'r' --> 'rectangle'")
    if shape_count > 1:
        print("Enter 'xxx' to show calculation history and exit program")
    # Ask user what shape they would like to select
    shape = in_list("Select shape: ", valid_shapes, "Error - Please enter rectangle, circle, "
                                                    "triangle or parallelogram")
    # exit code
    if shape == "Xxx":
        break
    print("Enter 'xxx' at any point to restart")
    # if shape is triangle of parallelogram ask for area/perimeter
    if shape == 'Triangle' or shape == 'Parallelogram':
        # instructions, area/perimeter
        if display_instructions == "Yes":
            print()
            print("Enter 'area' to calculate area of the shape, or 'perimeter' for perimeter\n"
                  "Shortcuts: 'a' for area, 'p' for perimeter")
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
    if area_perimeter != 'Xxx':
        # instructions for user to enter shape dimensions
        if display_instructions == "Yes":
            print()
            print("Enter the dimensions according to the diagram. e.g. 4, 78, 3.56\n",)
        print(shape_ascii[shape])
        # asks user for the dimensions of their shape
        dimension_history = dimension_q(subtract, "Error - Please enter a number between 0.01 and 999")
        # if the user exited the program during dimension input, scrap the previous inputs
        if dimension_history == 'xxx':
            if len(history[1]) != len(history[2]):
                history[1].pop()
            if len(history[0]) != len(history[1]):
                history[0].pop()
        else:
            # fills in the unused dimensions with blank space
            for c in range(1, len(dimension_history) + 1):
                if len(history[c]) < shape_count:
                    history[c].append('')
            shape_count += 1

            # instructions, unit of measurement
            if display_instructions == "Yes":
                print()
                print("Enter a unit of measurement.\n"
                      "e.g. km, m, cm, mm, i, mi, ft, yd.\n"
                      "You can type the full and shortened names, (kilometre, km)")
            # ask user for unit of measurement for their shape
            measurement = in_list("Unit of measurement: ", measurement_units,
                                  "Error - please enter km, m, cm, mm, i, mi, ft or yd.").lower()
            history[7].append(measurement)
        # does calculations with shape and dimensions, displays area and/or perimeter
            if area_perimeter == "Perimeter":
                perimeter = calculations(perimeter_formula[shape], "Perimeter: ", dimension_history, 6, measurement)
                history[5].append('')
            elif area_perimeter == "Area":
                area = calculations(area_formula[shape], "Area: ", dimension_history, 5, measurement)
                history[6].append('')
            else:
                area = calculations(area_formula[shape], "Area: ", dimension_history, 5, measurement)
                perimeter = calculations(perimeter_formula[shape], "Perimeter: ", dimension_history, 6, measurement)
            display_instructions = 'no'
            # adding shape to history dict
            history[0].append(shape)
            print()
# Display history instructions
print()
print("Enter 'yes' for full calculation history (all inputs and calculations), "
      "'no' for only calculations\nShortcut: 'y' for yes, 'n' for no")
# asking user if they want to display whole dataframe
full_display = in_list("Display whole dataframe?: ", yes_no, "Error - please enter yes or no")
history_dict = pandas.DataFrame(history_dict)
history_dict = history_dict.set_index('Shape')
print()
# display history dataframe
if full_display == 'Yes':
    print(history_dict)
else:
    print(history_dict[['Area', 'Perimeter', 'Unit']])

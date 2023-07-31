# functions

def num_check(num):
    # check if num is within range, 0 - 999
    if num == 'xxx':
        return 'exit'
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


def dimension_q(subtractor):
    inputted_dimensions = dimensions.copy()
    # use dict to ask user for dimension input
    if shape == "Triangle" and area_perimeter == "Area":
        b = list(range(0, 1)) + list(range(3, 4))
    elif shape == "Parallelogram" and area_perimeter == "Area":
        b = list(range(0, 1)) + list(range(2, 3))
    else:
        b = range(len(shape_dimensions[shape]) + subtractor)
    for i in b:
        # checking if input is valid and numerical
        validity = "Invalid"
        while validity == "Invalid":
            inputted_dimensions[i] = input(shape_dimensions[shape][i])
            validity = num_check(inputted_dimensions[i])
            if validity == 'exit':
                return 'xxx'
        # adding inputted dimensions to list
        if shape == 'Parallelogram' and i == 2:
            history[3].append(inputted_dimensions[i])
            # currently, inputted dimensions is wrong with parallelogram fix pls
        else:
            history[i].append(inputted_dimensions[i])
    return inputted_dimensions


history = [
        [],
        [],
        [],
        []
    ]

# dictionary with shape as key, dimensions
shape_dimensions = {'Rectangle': ['base: ', 'height: '],
                    'Circle': ['radius: '],
                    'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
                    'Parallelogram': ['base: ', 'sides: ', 'height: ']}

dimensions = ['x', 'y', 'z', 'a']

# list for valid area/perimeter responses
valid_area_perimeter = [
    ['area', 'a'],
    ['perimeter', 'p', 'per']
]

shape_count = 1


# loop 6 times for testing purposes
for x in range(0, 6):
    # for testing purposes, shape input is simple
    shape = input("select shape: ")
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
        area_perimeter = ''
    # add dimensions to list to display history at the end
    dimension_history = dimension_q(subtract)
    # if the user exited the program during dimension input, scrap the previous inputs
    if dimension_history == 'xxx':
        if len(history[0]) != len(history[1]):
            history[0].pop()

    else:
        for c in range(0, len(dimension_history)):
            if len(history[c]) < shape_count:
                history[c].append('n')
        shape_count += 1

    print(history)

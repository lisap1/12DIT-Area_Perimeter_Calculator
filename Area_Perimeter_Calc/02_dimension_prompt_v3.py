# functions
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
    # if subtractor == -1:
    for i in range(len(shape_dimensions[shape]) + subtractor):
        inputted_dimensions[i] = input(shape_dimensions[shape][i])
        history[i].append(inputted_dimensions[i])
    return history


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

dimensions = ['x', 'y', 'z', 'a']

# list for valid area/perimeter responses
valid_area_perimeter = [
    ['area', 'a'],
    ['perimeter', 'p', 'per']
]


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
    ap_history = dimension_q(subtract)
    # x = 3 - len(shape_dimensions[shape])
    # history[x].append(0)
    # print(dimension)

    # print(history)

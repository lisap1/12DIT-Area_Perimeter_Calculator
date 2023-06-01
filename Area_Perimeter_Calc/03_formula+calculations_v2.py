import math


# functions
# function for calculating area/perimeter
def formula_calc(formula, outcome, placement):
    calc = formula[shape]
    history[placement].append(str(calc)[1:-1])
    print(outcome + str(calc)[1:-1])
    return calc
# get list of formulas and dimensions
# try, except, run the calculations
# return area and/or perimeter calculations


# lists
inputted_dimensions = ['5', '3', '4', '2.41']

x = float(inputted_dimensions[0])
y = float(inputted_dimensions[1])
z = float(inputted_dimensions[2])
h = float(inputted_dimensions[3])

# for testing purposes, create list of inputted dimensions

dimensions = ['x', 'y', 'z', 'h']
# list for shapes and their corresponding formulas
shape_dimensions = {'Rectangle': ['height: ', 'base: '],
                    'Circle': ['radius: '],
                    'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
                    'Parallelogram': ['base: ', 'sides: ', 'height: '],
                    }

area_formula = {'Rectangle': [x * y],
                'Circle': [math.pow(x, 2) * math.pi],
                'Triangle': [(x * h)/2],
                'Parallelogram': [h * x]
                }

perimeter_formula = {'Rectangle': [2 * x + 2 * y],
                     'Circle': [2 * math.pi * x],
                     'Triangle':  [x + y + z],
                     'Parallelogram': [2 * x + 2 * y]
                     }


# create history list
history = [
        ['x'],
        ['y'],
        ['z'],
        ['h'],
        [],
        []
    ]

# main program
for q in range(0, 6):
    # basic shape selection
    shape = input("select shape: ")
    # run the calculation function with the inputted dimensions
    area = formula_calc(area_formula, 'Area: ', 4)
    perimeter = formula_calc(perimeter_formula, 'Perimeter: ', 5)

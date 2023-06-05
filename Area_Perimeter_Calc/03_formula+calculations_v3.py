# problem with the way my calculations are set out
# function that
# takes inputted dimensions
# takes formulas
# runs appropriate inputs with variables in formula

# problems
# variables in the formula lists are undefined
# does not take existing inputs and sub them into formula
#

# main program returns [2, 3, x, h]
# for float in [2, 3, x, h] ...

# imports
from sympy import symbols, pi


# functions go here
# function for calculating area/perimeter
def formula_calc(formula, outcome, placement):
    calc = formula[shape]
    history[placement].append(calc[1:-1])
    print(outcome + str(calc)[1:-1])
    return calc


# function for doing area and perimeter  calculations
# (store the formulas in a dictionary somewhere else make this function generic and reusable)
    # Area = calculator(x, y, h)
    # Perimeter = calculator(x, y, z)
# setting up dictionaries and lists
x = symbols('x')
y = symbols('y')
z = symbols('z')
h = symbols('h')

area_formula = {'Rectangle': x * y,
                'Circle': float(pi) * x ** 2,
                'Triangle': (x * h)/2,
                'Parallelogram': h * x
                }

perimeter_formula = {'Rectangle': 2 * x + 2 * y,
                     'Circle': 2 * float(pi) * x,
                     'Triangle':  x + y + z,
                     'Parallelogram': 2 * x + 2 * y
                     }

dimensions = ['5', '3', '4', '2.41']

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
    shape = input("select shape: ")
    # Calculations
    area = area_formula[shape].subs({x: dimensions[0], y: dimensions[1], z: dimensions[2], h: dimensions[3]})
    perimeter = perimeter_formula[shape].subs({x: dimensions[0], y: dimensions[1], z: dimensions[2], h: dimensions[3]})
    print("Area: " + str(round(area, 3)))
    print("Perimeter: " + str(round(perimeter, 3)))
    history[4].append(round(area, 3))
    history[5].append(round(perimeter, 3))
    print(history)
# Add to list

# Display history

# set up lists
valid_shapes = [
    ["rectangle", "rec", "rec", "r"],
    ["triangle", "tri", "t"],
    ["parallelogram", "para", "parallel", "p"],
    ["circle", "cir", "c"]
]


# functions
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


# Loop until valid answer
shape = ''
while shape != 'Xxx':
    shape = q_in_list("Select shape: ", valid_shapes, "Error - Please enter rectangle, circle, "
                                                      "triangle or parallelogram")
    print(shape)

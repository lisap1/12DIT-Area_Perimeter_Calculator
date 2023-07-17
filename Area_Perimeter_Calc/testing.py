def dimension_q(subtractor):
    inputted_dimensions = dimensions.copy()
    # use dict to ask user for dimension input
    if shape == "Triangle" and area_perimeter == "Area":
        for i in list(range(0, 1)) + list(range(3, 4)):
            validity = 'Invalid'
            while validity == "Invalid":
                inputted_dimensions[i] = input(shape_dimensions[shape][i])
                validity = 'valid'
    else:
        for i in range(len(shape_dimensions[shape]) + subtractor):
            # checking if input is valid and numerical
            validity = "Invalid"
            while validity == "Invalid":
                inputted_dimensions[i] = input(shape_dimensions[shape][i])
                validity = num_check(inputted_dimensions[i])
            print(inputted_dimensions)
        # adding inputted dimensions to list
        if shape == 'Parallelogram' and i == 2:
            history[3].append(inputted_dimensions[i])
        else:
            history[i].append(inputted_dimensions[i])
    return history, inputted_dimensions

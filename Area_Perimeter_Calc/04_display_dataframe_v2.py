import pandas


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


# list of expected outcomes to put in dataframe for testing purposes
history = [
    ['Rectangle', 'Circle', 'Triangle', 'Triangle', 'Parallelogram', 'Parallelogram'],
    [3, 3, 5, 5, 2, 2],
    [2, 'n/a', 3, 3, 3, 3],
    ['n/a', 'n/a', 4, 4, 'n/a', 1],
    ['n/a', 'n/a', 2.4, 'n/a', 'n/a', 'n/a'],
    [6, 28.27, 6, 'n/a', 'n/a', 2],
    [10, 18.85, 'n/a', 12, 10, 'n/a']
]

history_dict = {
    'Shape': history[0],
    'Base/Radius': history[1],
    'Side 1': history[2],
    'Side 2/Height': history[3],
    'Height': history[4],
    'Area': history[5],
    'Perimeter': history[6]
}

yes_no = [
    ['yes', 'y', 'ye'],
    ['no', 'n']
]

valid = False
while not valid:
    full_display = in_list("Display whole dataframe? ", yes_no, "Error - please enter yes or no")
    history_dict = pandas.DataFrame(history_dict)
    history_dict = history_dict.set_index('Shape')
    if full_display == 'Yes':
        print(history_dict)
    else:
        print(history_dict[['Area', 'Perimeter']])
    print()


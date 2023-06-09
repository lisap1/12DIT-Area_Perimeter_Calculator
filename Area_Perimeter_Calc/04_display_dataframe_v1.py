import pandas


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

history_dict = pandas.DataFrame(history_dict)
history_dict = history_dict.set_index('Shape')
print(history_dict)

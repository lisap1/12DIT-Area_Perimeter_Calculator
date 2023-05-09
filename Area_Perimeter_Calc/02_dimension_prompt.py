# dictionary with shape as key, dimensions, area formula, perimeter formula
shape_dimensions = {'Rectangle': ['height: ', 'base: '],
					'Circle': ['radius: '],
					'Triangle': ['base: ', 'side 1: ', 'side 2: ', 'height: '],
					'Parallelogram': ['base: ', 'sides: ', 'height: ']}

dimensions = ['x', 'y', 'z', 'a']
# list for valid area/perimeter responses

# if shape is triangle or parallelogram, ask if they want a/p

# use in_list for area/perimeter

# loop 6 times for testing purposes
for x in range(0, 6):
	# for testing purposes, shape input is simple
	shape = input("select shape: ")
	inputted_dimensions = dimensions.copy()
	# use dict to ask user for dimension input
	for i in range(0, len(shape_dimensions[shape])):
		inputted_dimensions[i] = input(shape_dimensions[shape][i])
	print(dimensions)
	print(inputted_dimensions)

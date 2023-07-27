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


measurement_units = [
    ['cm', 'centimeters', 'centi meters', 'centimetres', 'centi metres', 'centimeter'],
    ['m', 'meters', 'metres', 'meter'],
    ['in', 'inches', 'i', 'inch'],
    ['km', 'kilometers', 'kilometres', 'kilo meters', 'kilo metres', 'kilometer'],
    ['mi', 'miles', 'mile'],
    ['mm', 'millimeters', 'millimetres', 'millimeter', 'millimetre'],
    ['ft', 'feet', 'foot'],
    ['yd', 'yards', 'yard'],
]

loop = False
while not loop:
    measurement = in_list("Unit of measurement: ", measurement_units,
                          "Error - please enter a valid unit of measurement")
    print(measurement.lower())

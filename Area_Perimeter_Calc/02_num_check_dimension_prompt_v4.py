def num_check(num):
    # check if num is within range, 0 - 999
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
    # round num to 4 digits
    # allow floats and integers


valid = False
while not valid:
    number = input("Enter Number: ")
    validity = num_check(number)
    print(validity)

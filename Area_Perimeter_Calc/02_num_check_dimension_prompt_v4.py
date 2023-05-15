def num_check(num):
    # check if num is within range, 0 - 999
    if num.isdigit():
        if 0 < int(num) < 999:
            # num.round(num, 4)
            print(num)
            return "valid"
    return "Invalid"
    # round num to 4 digits
    # allow floats and integers


valid = False
while not valid:
    number = input("Enter Number: ")
    validity = num_check(number)
    print(validity)

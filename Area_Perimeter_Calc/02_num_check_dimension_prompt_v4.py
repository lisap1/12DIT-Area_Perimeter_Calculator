def num_check(num):
    # check if num is within range, 0 - 999
    print(num)
    try:
        if 0 < float(num) < 1000:
            # num.round(num, 4)
            num = round(float(num), 3)
            print(num)
            return "valid"
    finally:
        return "Invalid"
    # round num to 4 digits
    # allow floats and integers


valid = False
while not valid:
    number = input("Enter Number: ")
    validity = num_check(number)
    print(validity)

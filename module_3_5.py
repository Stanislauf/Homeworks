def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        res = first * get_multiplied_digits(int(str_number[1:]))
        return res
    else:
        return first


print(get_multiplied_digits(20305))
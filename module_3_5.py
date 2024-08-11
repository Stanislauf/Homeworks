def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith('0'):
        str_number = str_number[:-1]
    if len(str_number) > 1:
        res = first * get_multiplied_digits(int(str_number[1:]))
        return res
    else:
        return first

import re
regex = '^[0-9]+$'
number = str(input('Введите целое число: '))
pattern = re.compile(regex)
if pattern.search(number) is not None:
    print(f'Произведение цифр числа {number} равно: ', get_multiplied_digits(number))
else:
    number = str(input('Вы ввели недопустимые символы. Введите целое число: '))
    print(f'Произведение цифр числа {number} равно: ', get_multiplied_digits(number))

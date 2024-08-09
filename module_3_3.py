def print_params(car='BMW', price=7000000, result=True):
    print(car, price, result)


print_params()
print_params("PORSHE", 10000000)
print_params(car=8000000)
print_params(result=[0, 0, 9])

values_list = ["LADA", 11000000, False]
values_dict = {"price": 200000, "car": "MUSTANG", "result": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, "CHERRY"]
print_params(*values_list_2, 3000000)

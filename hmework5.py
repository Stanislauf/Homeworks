immutable_var = 345, 279, "corteo", True
print(immutable_var)
# immutable_var[3] = False -> Кортеж по определению неизменяемая упорядоченная коллекция
# print(immutable_var)
mutable_list = ["corteo", 34, 789, False]
print(mutable_list)
mutable_list[0] = "convoglio"
mutable_list[1] = mutable_list[2] // mutable_list[1]
mutable_list[2] = mutable_list[1] - mutable_list[2]
mutable_list[3] = True
print(mutable_list)
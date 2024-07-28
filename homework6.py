my_dict = {"Vasya" : 1998, "Petya" : 2001, "Kolya" : 1996}
print(my_dict)
print("Existing value: ", my_dict.get("Petya"))
print("Not existing value: ", my_dict.get("Pepe"))
my_dict.update({"Vaha" : 2005, "Maga" : 2004})
print(my_dict)
del_ = my_dict.pop("Kolya")
print("Deleted value: ", del_)
print(my_dict)

my_set = {1, 1, 34.56, True, "строчка", "строчка"}
print("Set: ", my_set)
my_set.add("qiorno")
a = (1, 2, 3, 1, 2, 3)
my_set.add(a)
print(my_set.remove(a))
print("Modified set: ", my_set)





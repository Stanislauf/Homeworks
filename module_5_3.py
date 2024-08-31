class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует!")
        else:
            for i in range(1, new_floor +1):
                print("Этаж - ", i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __lt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
"""
h1.go_to(5)
h2.go_to(10)
print(len(h1))
print(len(h2))
"""
print(str(h1))
print(str(h2))
print(h1 == h2)
h2 = h2.__add__(16)
print(str(h2))
print(h1 == h2)
print(h1.__iadd__(10))
print(h2.__radd__(10))
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


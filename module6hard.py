from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = list(sides * self.sides_count)
        self.field = False



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g ,b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if isinstance(i, int) and i > 0 and len(new_sides) == self.sides_count:
                return True
            else:
                return False
            # return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count
    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__sides = [sides[0]] * self.sides_count

    def get_volume(self):
        v = self.__sides[0] ** 3
        return v
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.sides = sides
        self.__sides = [sides[0]] * self.sides_count


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((50, 50, 50), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

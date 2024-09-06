class Animal:
    alive = True # живой
    fed = False # накормленный
    def __init__(self, name):
        self.name = name


class Plant:
    edidle = False  # съедобность
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __str__(self):
        return self.name
    def eat(self, food):  # food - это параметр, принимающий объекты классов растений
        self.food = food
        if food.edidle == False:
            print(f'{self.name} не стал есть {self.food}' )
            self.alive = False
        else:
            print(f'{self.name} съел {self.food}')
            self.fed = True
class Predator(Animal):
    def __str__(self):
        return self.name
    def eat(self, food):  # food - это параметр, принимающий объекты классов растений
        self.food = food
        if food.edidle == False:
            print(f'{self.name} не стал есть {self.food}' )
            self.alive = False
        else:
            print(f'{self.name} съел {self.food}')
            self.fed = True
class Flower(Plant):
    def __str__(self):
        return self.name

class Fruit(Plant):
    edidle = True
    def __str__(self):
        return self.name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a2.name)
print(p2.name)
print(a1.alive)
print(a2.fed)



a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

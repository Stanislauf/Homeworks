class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self):
        self.x_distance = self.x_distance + self.dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self):
        self.y_distance = self.y_distance + self.dy

class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        super().run()
        super().fly()
    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos
    def voice(self):
        print(super().sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice() # если сначала будет стоять наследованный класс Horse то sound будет Frrr, а в задаче написано
# что I train, eat, sleep, and repeat, в задаче получается нестыковка
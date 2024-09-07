class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
    def get_model(self):
        return f'Модель - {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя - {self.__engine_power}'
    def get_color(self):
        return f'Цвет - {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец - {self.owner}')
    def set_color(self, new_color):
        self.new_color = str(new_color)
        if new_color.lower() in self.__COLOR_VARIANTS:
            print('___________________________________________________________________')
            print(f'Производится замена цвета {self.__color} на новый цвет {new_color} ...')
            print('-------------------------------------------------------------------')
            self.__color = new_color
        else:
            print(f"Невозможно заменить старый цвет {self.__color} на новый {new_color} так как его нет в списке допустимых")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5





vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue', )
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()


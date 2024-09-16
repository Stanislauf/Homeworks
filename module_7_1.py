from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}\n"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file_pr = open(self.__file_name, 'r')
        pr_str = file_pr.read()
        file_pr.close()
        return pr_str

    def add_product(self, *products):
        existing_products = [line.split(', ')[0] for line in self.get_products().strip().split('\n') if line] # мы получаем
        # список названий существующих продуктов, которые хранятся в файле. Названия этих продуктов используются позже,
        # чтобы проверить, существуют ли они уже, перед добавлением новых продуктов
        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file_pr = open(self.__file_name, 'a')
                file_pr.write(str(product))
        #file_pr.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add_product(p1, p2, p3)

print(s1.get_products())


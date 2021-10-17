# Мысли в слух:
# Результаты работы будет оценка мнения студента по 10 бальной шкале,
# каждый курс/пакет курсов имеет свою цену и значимость по 5 бальной шкале
from random import random
from simple_draw import random_number

SCALE_SIGNIFICANCE = 5
ESTIMATED_OPINION = 10
MAX_PRICE_COURSES = 5500
CURATOR = 1500


class Product_price:
    def __init__(self, param_1, param_2, param_3):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        self.course_package = {'pm_12': 0, 'pm_23': 0, 'pm_31': 0}


    def price_determination(self):
        self.param_1.price = (MAX_PRICE_COURSES * self.param_1.significance) // SCALE_SIGNIFICANCE
        self.param_2.price = (MAX_PRICE_COURSES * self.param_2.significance) // SCALE_SIGNIFICANCE
        self.param_3.price = (MAX_PRICE_COURSES * self.param_3.significance) // SCALE_SIGNIFICANCE
        print(f'1 - {self.param_1.price}\n'
              f'2 - {self.param_2.price}\n'   
              f'3 - {self.param_3.price}')

    def price_package_manual(self, discount):
        self.course_package['pm_12'] = round((self.param_1.price + self.param_2.price) * discount) + CURATOR
        self.course_package['pm_23'] = round((self.param_2.price + self.param_3.price) * discount) + CURATOR
        self.course_package['pm_31'] = round((self.param_3.price + self.param_1.price) * discount) + CURATOR


    def __str__(self):
        pass


class Product:
    def __init__(self, name, significance):
        self.name = name
        self.significance = significance
        self.price = 0

    def __str__(self):
        pass


class Man:
    def __init__(self, name, min_spend, max_spend, product_price):
        self.min_spend = min_spend
        self.max_spend = max_spend
        self.satisfaction = 0
        self.product_price = product_price
        self.name = name


    def buy_product(self):
        mean_cash = (self.max_spend - self.min_spend) // 10
        random_event = random_number(1, 3)
        if random_event == 1:
            self.satisfaction = self.product_price.course_package['pm_12'] // mean_cash
        elif random_event == 2:
            self.satisfaction = self.product_price.course_package['pm_23'] // mean_cash
        elif random_event == 3:
            self.satisfaction = self.product_price.course_package['pm_31'] // mean_cash
        print(random_event)


    def __str__(self):
        return f'Я - {self.name}. Моя оценка - {self.satisfaction}'



py_pro = Product(name='py_pro', significance=4.2)
py_start = Product(name='py_start', significance=3.2)
js_basics = Product(name='js_basics', significance=1.2)
test = Product_price(param_1=py_pro, param_2=py_start, param_3=js_basics)
test.price_determination()
test.price_package_manual(discount=0.7)
print(test.course_package)
man_1 = Man(name='1', min_spend=2000, max_spend=10000, product_price=test)
man_1.buy_product()
print(man_1)

man_list = []

for person in range(1, 11):
    person = Man(name=person, min_spend=random_number(2000, 4000), max_spend=random_number(5000, 7000), product_price=test)
    man_list.append(person)

for man_name in man_list:
    man_name.buy_product()
    print(man_name)

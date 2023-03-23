class A:
    def instance_method(self):
        print("метод обькта")
        print("self", self)

pop =A()
pop.instance_method()
# метод обькта
# self <__main__.A object at 0x7fcb7c157af0>
# когда мы вызываем метод у обекта, то нам не нужно передавать его в self, он передается автоматически 

A.instance_method(pop) # тоже самое что выше

#-------------------------------------------------------------------------------------------

class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)


A.class_method()

# метод класса
# cls <class '__main__.A'>

pop1 =A()
pop1.class_method()

# метод класса
# cls <class '__main__.A'>
# все равно откуда вы будите вызывать класс-метод (от обьекта или от класса) первым аргументом все равно будет приходить класс


#   Примеры:

class C:
    counter = 0

    def __init__(self):
        # обьект создается 
        # C.counter += 1
        self._inc_counter()

    def __del__(self):
        # обьект удаляется
        # C.counter -= 1 
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        # cls - class C
        # увиличиваем атрибут класса counter на один
        cls.counter += 1


    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1


pop1 = C()
pop2 = C()
pop3 = C()
pop4 = C()
print(C.counter) # 4
del pop4
print(C.counter) # 3

class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ing = ingredients

    def cook(self):
        print(f"Пиица размером {self.r * 2}")
        print(f"Ингридиенты: {self.ing}")

    @classmethod
    def four_cheeze(cls, radius):
        pizza = cls(radius, "Сыр", "Колбаска", "Помидорки")
        #pizza = Pizza(15, "Сыр", "Колбаска", "Помидорки")
        return pizza


pizza1 = Pizza(15, "Сыр", "Колбаска", "Помидорки")
pizza1.cook()
# Пиица размером 30
# Ингридиенты: ('Сыр', 'Колбаска', 'Помидорки')

pizza2 = Pizza(20, "Сыр 1", "Сыр 2", "Сыр 3", "Сыр 4")
pizza2.cook()

pizza3 = Pizza(20, "Сыр", "Колбаска", "Помидорки")
pizza3.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()
# Пиица размером 20
# Ингридиенты: ('Сыр', 'Колбаска', 'Помидорки')

#-----------------------------------------------------------------------------------------------------------------


class A:
    @staticmethod
    def static_method():
        print("статик метод")

ppp = A()
ppp.static_method()   # статик метод

class Cylinder:
    def __init__(self, diametr, height):
        self.di = diametr
        self.h = height
        self.area = self.get_area(diametr, height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circ_area = pi * di**2 / 4
        side_area = pi * di * h
        return circ_area*2 + side_area


cylinder1 = Cylinder(4, 10)
print(cylinder1.area)   #150.79644737231007

print(Cylinder.get_area(4,10))   #150.79644737231007
# получили ту же информацию только без создания обьекта 
#------------------------------------------------------------------------------------------------------

class Makers:
    language_choices = "Python", "Makers"
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"Hello, {self.name}"
    
    @classmethod
    def class_method(cls):
        return f"Welcome to Makers! What type of language do you choose?:  {cls.language_choices}"
    
    @staticmethod
    def static_method(choice):
        return f"Great! You chose {choice} course"
    

user1 = Makers(name="Robert")
print(user1.instance_method())
print(user1.class_method())
print(user1.static_method(choice="Python"))





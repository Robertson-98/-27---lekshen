"===================================Миксины======================================"

# Это классы, которые будут использоваться для наследования.
# Но от мексинов не создаются классы

# Миксины - классы-примеси, которые служат для расширения функционала класса.
#1. От мексинов нельзя создать обьекты, поскольку мексины - несамостоятельные классы
#2. При наследовании миксины должны идти в первую очередь

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class FlyMixin:
    def fly(self):
        print('я могу летать')


class Human(WalkMixin, SwimMixin):
    name ='человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'


class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'


obj_h = Human()
setattr(obj_h, 'new_attribute', 'hello world')
print(dir(obj_h))
print(obj_h.new_attribute)




object = [Human(), Fish(), Exocoetidae(), Duck()]

for i in object:
    # print(i.name)
    attrs = ["fly", "swim", "walk", "talk"]
    for attr in attrs:
        if hasattr(i,attr):
            pop1 = getattr(i,attr)
            pop1()

# hasattr - Функция, которая принимает обьект и название фттрибута. Возвращает True, если у обьекта есть такой аттрибут (метод)
# getattr - Функция, которая принимает обьект и название оттрибута. Возвращает значение аттрибута
# setattr - Функция, которая принимает обьект и название оттрибута. Добовляет в обьект новый аттрибут или перезапишет одноименный аттрибут


# pop3 = Duck()
# print(hasattr(pop3, 'fly'))  # True
# pop4 = getattr(pop3, 'walk')
# pop4()


#--------------------------------------------------------------------------------------------------------------
# pop3.fly()
# pop3.swim()
# pop3.walk()



# pop2 = Exocoetidae()
# pop2.swim()
# pop2.fly()


# pop1 = Human()
# pop1.talk()
# pop1.walk()


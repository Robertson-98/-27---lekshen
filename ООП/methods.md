# class/static/instance methods
> instance method -методы, которые первым аргументом принимают ссылку на обьект откласс (instance,self).  Используются они для работы с обьектом и его аттрибутами


```py
class A:
    def instance_method(self):
        print("метод обькта")
        print("self", self)

pop =A()
pop.instance_method()
```

>  **class methods** - методы, которые первым аргументом принимают класс (cls).  Используются они для работы с классом и его аттрибутами

```py

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
```

> для создания class метода, нужнл использовать декоратор "@classmethod"


# **static method** - методы которые не взаимодействуют с обьектом и классом, но находятся внутри класса( по принципу инкапсуляции (все, что нужно для работы класса лежит внутри самого класса))


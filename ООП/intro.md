# OOP
> ООП - обьектно ориентированное программирование (парадигма)

> Создание класса 
```py
class Person:
    #переменные внутри класса - это аттрибуты
    arms = 2
    legs = 2

    #функции внутри класса - это методы
    def walk():
        print("я хожу брат")

```
## Обьекты класса
> обьект, экземпляр, instance - обьект, который создан по шаблону класса(он перенимает все аттрибуты и методы класса)

```py
class A:
    var1="переменная класса"

    def __init__(self):
        self.var2 = "переменная обьекта"
```
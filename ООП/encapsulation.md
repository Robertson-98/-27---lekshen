# Инкапсуляция - принцип ООП
> у которого есть 2 трактовки:
1. все что нужно для работы класса - лежит в классе
2. ограничение доступа к аттрибутом(сокрытие данных)

# в питоне есть 3 доступа ввида:
1. public (публичный)
2. proteccted(защищенный) - когда один underscore в начале
3. private (приватный)   - когда два underscore а начале


> В Python инкапсуляция реализованна на уровне соглашение



# Getters / Setters
> методы с помощью которых мы указываем каким образом мы можем получать и изменять какие-то аттрибуты


## Property
> декоратор, который превращает метод в аттрибут с декораторами: getter, setter, deleter

> Setter - будет вызываться, когда мы записываем в атрибут значение
> Deleter - будет вызываться, когда мы удаляем фттрибут через del

```py

class Person:
     
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")    

    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception("Cannot delete age")
        del self.__age

obj = Person("Robert", 15)
print(obj.age)
obj.age = 25
print(obj.age)
# obj.age = -100  #Exception: Invalid age
# del obj.age #Exception: Cannot delete age
obj.age = 115
del obj.age
```
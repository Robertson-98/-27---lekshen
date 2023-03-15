from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod             #проверяет если метод удочернего класса, если нету то он ругается
    def speak(self):      
        pass

class Dog(AbstractAnimal):
    pass

#obj = Dog()   #TypeError: Can't instantiate abstract class Dog with abstract method speak  - ругается)

class Dog(AbstractAnimal):
    def speak(self): 
        print("гав-гав")


obj = Dog()     #ругаться не будет потому что есть похожие методы который мы проверяем
obj.speak()
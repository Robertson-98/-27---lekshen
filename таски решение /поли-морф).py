##===================1

a = '12342342345' 
b = [1,['a',5,6],2,3,4,5] 
c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
for i in [a,b,c]:
    print(len(i))

##===================2

class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

def to_pet(i):
        return i.voice()
   
barsik = Cat()
rex = Dog()
to_pet(barsik) 
to_pet(rex)

##===================3

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}")

class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status

    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}")

class Student(Person):
    def __init__(self, name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course

    def get_info(self):
        print(f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе")

def get_human_info(i):
        return i.get_info()

person = Person("Иван", "Петров")
employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
student = Student("Иван", "Петров", "КГТУ", "3")

get_human_info(person) 
get_human_info(employee) 
get_human_info(student) 

##=====================4

from abc import ABC, abstractmethod 
from math import pi 
class Shape(ABC): 
    @abstractmethod 
    def get_area(self): 
        pass 
    
class Triangle(Shape): 
    def __init__(self, base, height): 
        self.base = base 
        self.height = height 
        
    def get_area(self): 
        return self.base * self.height * 0.5 
    
class Square(Shape): 
    def __init__(self, length): 
        self.length = length 
        
    def get_area(self): 
        return self.length ** 2 
    
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
        
    def get_area(self): 
        return pi * self.radius ** 2 
    
triangle = Triangle(5, 5) 
square = Square(5) 
circle = Circle(4) 
print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area())

##=======================5

class OS:
    def __init__(self, version): 
        self.version = version

class Windows(OS):
    def copy(self, text):
        return f"скопирован текст '{text}' горячими клавишами CTRL + C"
class MacOS(OS):
    def copy(self, text):
        return f"скопирован текст '{text}' горячими клавишами COMMAND + C"
class Linux(OS):
    def copy(self, text):
        return f"скопирован текст '{text}' горячими клавишами CTRL + SHIFT + C"

win = Windows("10")
mac = MacOS("Big Sur")
lin = Linux("Ubuntu")

print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))


##=========================6
class Language:
    def __init__(self, level, type):
        self.level = level
        self.type = type

class Python(Language):
    def write_function(self, func_name, arg):
        return f"def {func_name}({arg})"
        
    def create_variable(self, var_name, value):
        return f"{var_name} = {value}"


class JavaScript(Language):
    def write_function(self, func_name, arg):
        return f"function {func_name}({arg}) {{ }}"
    
    def create_variable(self, var_name, value):
        return f"let {var_name} = '{value}'"


py = Python('Intermediate', 'Backend')
js = JavaScript('Advanced', 'Frontend')

print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

print(js.write_function('validate', 'form')) 
print(js.create_variable('password', 'john@123'))

#----------------------------------------------------------------------------------------------------------------------
class Language: 
    def __init__(self, level, type) -> None: 
        self.lvl = level 
        self.type = type 
        
class Python(Language): 
    def write_function(self, func_name, arg): 
        return f"def {func_name}({arg}):" 
        
    def create_variable(self, var_name, value): 
        if isinstance(value, str): 
            return f"{var_name} = '{value}'" 
            
        else: return f"{var_name} = {value}" 
        
class JavaScript(Language):
    def write_function(self, func_name, arg): 
        return f"function {func_name}({arg}) {{ }};" 
        
    def create_variable(self, var_name, value): 
        if isinstance(value, str): 
            return f"let {var_name} = '{value}';" 
        
        else: return f"let {var_name} = {value};" 
        
py = Python('Intermediate', 'Backend') 
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John')) 

js = JavaScript('Advanced', 'Frontend') 
print(js.write_function('validate', 'form')) 
print(js.create_variable('password', 'john@123'))



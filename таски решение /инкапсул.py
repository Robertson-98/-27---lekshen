##=========================1

class A:
    def public(self):
        return("Public method")

    def _protected(self):
        return("Protected method")

    def __private(self):
        return("Private method")

    def get_protected(self):
        self._protected()

    def get_private(self):
        self.__private()
obj1 = A()
print(obj1.public())
print(obj1.get_private())
print(obj1.get_private())

##=======================2

class A:
    def method1(self):
        print("Hello World")

class B(A):
    pass

b1 = B()
b1.method1()

##======================3

class Car:
    __speed = 0 

    def set_speed(self, new):
        self.__speed = new
        return self.__speed

    def show_speed(self):
        return self.__speed

car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed())       

##======================4

class Car:
    __speed = 0 

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new):
        self.__speed = new
        return self.__speed

car1 = Car() 
print(car1.speed) 
car1.speed = 20
print(car1.speed)       

##=======================5


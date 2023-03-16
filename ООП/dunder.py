# dunder (double underscore) - методы у которых 2 _ в начале и в конце
# Магия - этих методов в том что мы не вызывем их на прямую

class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)
        
    def __init__(self):
        print("__INIT__")
        pass

A()
# __NEW__
# __INIT__

#__new__, __init__ - вызываются при создании обьекта

print(dir(object))
#['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __add__ +
# __sub__ -
# __floordiv__ /
# __truediv__ //

class A:
    pass
#__str__ str, print
print(A())   #<__main__.A object at 0x7f19b775bac0>

class A:
    def __str__(self) -> str:
        return "Hello"        #
    
print(A())  #Hello



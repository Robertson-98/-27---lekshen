class Dog:
    def speak(self):
        print("гав-гав")


class Cat:
    def speak(self):
        print("мяу-мяу")

class Frog:
    def speak(self):
        print("ква-ква")


animals = [Cat(), Frog(), Dog(), Frog(), Dog(), Cat()]

for i in animals:
    i.speak()

# мяу-мяу
# ква-ква
# гав-гав
# ква-ква
# гав-гав
# мяу-мяу

list1 = [1,2,3,4,5]
dict1 = {"a":1, "b":2}

list1.pop(0)   #удаление по индексу
dict1.pop("a") #удаление по ключу

#__add__
a = 4
b = 5
print(a.__add__(b)) #сложение  = 9
list2 = [1,2,3]
print(list1 + list2)   #[2, 3, 4, 5, 1, 2, 3]

#__len__

b = [1,2,3,[4,5,6]]
print(len(b))        #4
print(b.__len__())   #4
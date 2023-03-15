# Полиморфизм
> Принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разная реальзация)



```py
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
```
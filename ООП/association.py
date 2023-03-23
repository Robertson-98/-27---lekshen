class Battery:
    power = 100
    
    def charge(self):
        if self.power < 100:
            self.power = 100


class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()
        # когда мы создаем обькт от другого класса прям внутри другого -это называется композиция 

iphone = Iphone("золотой")
# Обьект батарейки удаляется вместе с обьектом iphone

print(iphone.battery.power)

del iphone
print(iphone)


#---------------------------------------------------------------------------------------------------------------------------------
class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # Когда мы принимаем уже созданный вне класса обьект - это называется агрегация 


battery = Battery()
nokia = Nokia("черный", battery)

print(nokia.battery.power)
del nokia

# удаляется только обьект Nokia

print(battery.power)

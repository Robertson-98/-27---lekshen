gen = (x for x in range(10))
print(gen)
# <generator object <genexpr> at 0x7f16570d2420>

def generator(n):
    for i in range(1, n+1):
        yield i**2

# print(generator(10))
# <generator object generator at 0x7ff7bc65e490>

# gen = generator(10)
# print(next(gen)) # 1
# print(next(gen)) # 4
# print(next(gen)) # 9
# print(list(gen)) # [16, 25, 36, 49, 64, 81, 100]

for i in generator(5):
    print(i)
# 1
# 4
# 9
# 16
# 25

gen = generator(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

#1 4 9 16 25 36 49 64 81 100 121 144 169 196 225

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __len__(self):
        return len([i for i in self])
    
    def __getitem__(self, index):
        return [ i for i in self][index]



a = IterInt(1234567)

for i in a:
    print(i)

print(8 in a)  #False
print(5 in a)  #True
print(len(a))  # 7
print(a[5])    # 6
print(a[1:4])  #[2, 3, 4]


string1 = "abcdefgi"
string2 = "abdbdh"
print(string1 > string2)

class MyStr():
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)
    
    def __le__(self, other):
        return len(self) <= len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)
    
    def __ne__(self, other):
        return len(self) != len(other)

string1 = MyStr("abdbdh")
string2 = MyStr("abcdefgi")
print(len(string1))
print(string1>string2)


class A:
    attr1 = "aaa"

    def __getattribute__(self, name):
        print("__getattribute__:", name)
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print("__setattr__:", name, value)
        return super().__setattr__(name, value)

    def __delattr__(self, name):
        print("__delattr__:", name)
        return super().__delattr__(name)
    
obj = A()
obj.attr1 #__getattribute__: ("attr1")
obj.attr1 = 'bbbb' # __setattr__: ("attr1" "bbbb")
del obj.attr1
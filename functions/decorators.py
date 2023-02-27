"=====================================Декоратор========================================="
#Декоратор- это функция высшего порядка, которая нужна чтобы расширять функционал другой функции, не меняя её.

def decorator(func):
    def wrapper():
        print("Функция вызывается")
        func()
        print("Функция завершила работу")
    return wrapper

def func():
    print("hello")

res = decorator(func)
print(res)                        #<function decorator.<locals>.wrapper at 0x7f3fbd1fa4d0>

res()
# Функция вызывается
# hello
# Функция завершила работу

"====================================Синтасический сахар======================================"

def decorator(func):
    def wrapper():
        print("Функция вызывается")
        func()
        print("Функция завершила работу")
    return wrapper


@decorator             # func = decorator(func)
def func():
    print("hello")
func()
# Функция вызывается
# hello
# Функция завершила работу

print(func)             #<function decorator.<locals>.wrapper at 0x7ff84893a710>

#-------------------------------------------------------------------------------------------------

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)


#---------------------------------------------------------------------------------------------------

from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"Функция отработала за {end-start}")
    return wrapper

from functools import cache         #позволяет записывать результат и при необходимости их вспоминает)

@timer
@cache
def func(count):
    for i in range(count):
        print(i)

# func(200000)           #Функция отработала за 0:00:01.270966

#-----------------------------------------------------------------------------------------------------

# <b>text</b>  - жирный текст
# <i>text</i>  - кусовом текст

def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

@bold
@italic
def func(string):
    return f'Hello {string}'
# func = bold(italic(func))

print(func('Makers'))




















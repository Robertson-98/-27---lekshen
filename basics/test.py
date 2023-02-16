# # inp1 = int(input('vvedite: '))
# # print(inp1)

# # import math
# # radius = 7 
# # s = pow(radius,2) * math.pi
# # print(s)


# # num = 7
# # p = num *4
# # s = num * num
# # print(p, s)

# num = int(input ("Введите число:"))
# if num > 0:
#     print(f"число {num} - положительное")
# elis num  == 0:
#     print(f"число {num} - этто 0")
# else


# #============================================================================================

# password = input ("придумайте свой пароль: ")
# first_let = password[0].upper()
# print(first_let)

# if len(password) <= 8:
#     print("Ваш пароль меньше 8 символов")                 #- код для создания пароля.

# elis not password.startswith(upper_let):
#     print("Ваш пароль не начинается с большой буквы") 

# else:
#     print( "Успешно создан пароль")
# ============================================================================================
#                       ТЕРНАРНЫЕ ОПЕРАТОРЫ

#  num = int(imput())

#  res ="HELLO" if num == 5 else "bye"
#  print(res)                     
# =======================================================================================

# num = ist(input())

# if num % 3 == 0 and num % 5 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# elif num % 3 == 0:
#     print    
#--------------------------------------------------------------------------------------------

# pop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reversed(pop))

# pop ="hello"
# chr
#----------------------------------------------------------------------------------------------

# string = 'Hello!'
# res = []
# for i in string:
#     res.append(ord(i))
# print(res)
# # print(ord('s'))

#-----------------------------------------------------------------------------------------------
# mark = int(input())
# if mark >= 90:
#     print("Отлично, Bаша оценка 5!")
# elif mark >= 80:
#     print("Здорово, Ваша оценка 4!")
# elif mark >= 70:
#     print("Хорошо, Ваша оценка 3!")
# elif mark >= 60:
#     print("Вам стоит подучить материал")
# else:
#     print("Вы не сдали экзамен")
#-----------------------------------------------------------------------------------------------
# number = 0.1
# if number < 0:
#     print("negative")
# if number > 0:
#     print("positive")    
# elif number == 0:
#     print("zero")
#--------------------------------------------------------------------------------------------

# list1 = [ 1,2,3,1,2,4,5,9,1,1,5,7,7]
# while 1 in list1:
#     list1.remove(1)
# print(list1)
#-------------------------------------------------------------------------------------------------
# pop = 87
# print(("negative", "positive")[pop>=50])
 #-------------------------------------------------------------------------------------------
# greeting = input()
# if greeting == "Hi":
#     print("здарова заебал")
# else :
#     print("NO")
#--------------------------------------------словари-----------------------------------------------
# dict1 = {"a":1, "b":2, "c":3}                        #первый способ поменять ключи со ззначениями
# res = {}
# for key, value in dict1.items():
#     res[value] = key
# print(res)


# dict3 =dict(zip(dict1.values(), dict1.keys()))      #второй способ поменять местами ключи и значения 
# print(dict3)
#-------------------------------------------------------------------------------------------
# import itertools
# list1 = [1,2,3]
# print(list(itertools.combinations(list1)))

 #14 logik
# lang = "kg"
# if "en" in lang:
#     print('This is english')
# elif "ru" in lang:
#     print('Это русский')
# elif "de" in lang:
#     print('Das ist Deutsch')
# elif "kg" in lang:
#     print('Бул кыргыз тили')

# #19 logik
# pop1 = input()
# if pop1.isdigit():
#     print("is digit")
# elif pop1.isalpha():
#     print("is alpha")
# else:
#     print("is ASCII")
# 
#########  --------------------------------------------------------- Калькулятор
print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Выберите дейсвие (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        if s == '+':
            pop1 = x + y
            print(f"Сумма = {pop1}")
        elif s == '-':
            pop1 = x - y
            print(f"Разность = {pop1}")
        elif s == '*':
            pop1 = x * y
            print(f"Произведение = {pop1}")
        elif s == '/':
            if y != 0:
                pop1 = x / y
                print(f"Частное = {pop1}")
            else:
                print("Делить на ноль нельзя!!!")
    else:
        print("Неверный знак операции!")
"=================================================================================================="
# while True:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     s = input("Выберите дейсвие (+,-,*,/): ")
#     if s == "0":
#         break




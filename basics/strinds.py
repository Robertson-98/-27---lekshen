"============================Строки=========================="
# Строки - этот неизменяемый тип данных, преднозначеный для хранения текста (последовательности символов)

sting1 =  'строка в одинарных ковычках'
string2 = 'строка в двойных ковычках '
string3 =  "don't"
string4 =  'Study in "Makers Incubator"'
string5 =  '''многострочный текст, на несколько строк и можно использовать любые ковычки '''

string6 = "hello" + " " + "world" # "hello world"
string7 = "hello" * 3 # "hellohellohello"
string8 = "HELLO " * 3 # "hello hello hello"

"============================Экранизация строк========================"
'\n' # перенос строки на новую строку
'\t' # отступ (табуляция)
'\ ' # отображение слэша (\)
'\\' # отображение слэша (\)
'\'' # отображение (')
"\"" # отображения (")
'\r' # перенос каретки в начало строки 

print("1234567\rhello")
 # hello67

'\v' # перенос на новую строку со смещение вправо на длину предыдущей строки 

print("hello\vworld") 
#hello
    # world 

"==========================Индексы====================="
# Индекс - Порядковый номер символа в строке (начиная с 0)
string = 'h e l l o'
        # 0 1 2 3 4
        #      -2-1

print(string[-1]) # 'o'
print(string[0])  # 'h'


string1 = 'hello world'
# срез -часть строки
print(string[6:9]) # "wor"

print(len(string1)) #11 - счиатет количество строк

string1[7:]  # 'orld'
string1[:]   # 'hello world'
string1[0:11:2]  # 'hlowrd'
string1[]


"===================================Форматирование строк=========================="
title = "пирог"
price = 35
string = f"Название: {title}, цена: {price}"
#  Название: пирог, цена: 35


format1 = "Название: %s, цена: %s"
print(format1 % ("яблоко", 80))
# Название: яблоко, цена: 80


format2 = "Название: {}, цена: {}"
print(format2.format("Груша", 60))
#


"===============================Методы строк========================================="
# Метод - это фунция которая пренадлежит определенному типу данных, к ней мы оброщаемся через точку
print(dir(str)) -#  посмотреть все  доступные методы для данного типа данных
print("hello".upper()) # "HELLO"
print("HELLO".lower()) # "hello"
print("HELLO world".swapcase()) # "hello WORLD"
print("hello world".capitalize()) # "Hello world"
print("hello world".title()) # "Hello World"
print("hello".center(11)) # ставит слово по середине 11 символов 
print("hello".center(11, "-")) # "---hello---"
print("Hello".count("l")) # 2
print("Hello".count("hello")) # 0
print("hello".count("")) # 6
print("hello world".split()) # ["hello", "world"]
print("hello world".split('o')) # ["hell", "w", "rld"]
print(" ".join(["hello", "world"])) # "hello world"
print("&".join(["hello", "world"])) # "hello&world"
print("hello world".find("wor")) # 6 - показывает с какой индекса начинается фраза

#   - идет комментарий 
"==================переменные================="
num1 = 8
num2 = 10 
print(num1+num2) # 18
# переменные - это именнованые ссылки на ячейки памяти, где хранятся какие-то данные, для дальнейшего использования ,при обращение название переменной.
"===================================Ввод и вывод данных====================="
number = input ("Введите число:  ")
print ("Введенное число -", number)
  # Input - функция которая позволяет принимать данные с терминала
  # Print - фунция которая позволяет выводить данные с терминала

"============================Правила наименования переменных================"
а = 5 #  можно, но не  совсем понятно  
# 1num = 10 # Нельзя начинать с чисел 
hello_world = "hello world" # для разделения используется только _
print = print # нельзя называть переменные уже встроенными названиями 
# if = 4 не получится использовать в качестве переменных ключевые слова
  

  # Snake Case - python  стиль написания переменных 
#   helloworldaaabbb 

  # Camel Case - стиль написания переменных во всех других языках 

"==============Типы данных в PYTHON ======================="
   # неизменяемые  
int_= 17 #целые числа
float_= 34.0 #не целые числа 
str_= "hello123"  #текстовый
bool_1= True #правда
bool_2= False  #лож 
none_= None #не знаем что придет
tuple_= (1,2,3,4,5,6,7,8,9,10)
# изменяемые 
list_= [1,2,3,4,5,6,7,8,9,10]  #список 
set_={1,2,1,4} #{1,2,4}       множество 
dict_= {'a':1,'b':2,'3':3}
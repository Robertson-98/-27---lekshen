"============================================List========================================"
# список -это изменяемый интерируемый индексируемый и упорядоченый тип данный,
# предназначеный для хранения элементов в строгом порядке!

list1 = [10, 3.5, "hello", [1, 2, 3], (1, 2), None, True, False]

list1[0]  #10
list1[3]  #[1, ,2 , 3]
list1[3][-1] # 3 
list1[-1] # False
list1[2][-1] # "o"

list2 = list("hello")
print(list2) #["h", "e", "l", "l", "o"]

list3 = list(range(3, 10, 2))
print(list3) #(3, 5, 7, 9)
print(list(range(5)))  # [0, 1, 2, 3, 4]

 #range - работает  только с числами
"=========================================Изменяемость=============================="

list12 = []
list12.append(1)
list12.append(2)
list12.append(3)
print(list12) # [1, 2, 3]

"=======================================Перебор элементов==============================="
#Перебор элементов Для перебора элементов можно использовать как цикл for, так и цикл while.
#Перебор с помощью цикла for:

companies = ["Microsoft", "Google", "Oracle", "Apple"] 
for item in companies: 
    print(item)

# Microsoft 
# Google 
# Oracle 
# Apple 

#Здесь вместо функции range мы сразу можем подставить имеющийся список companies.
#Перебор с помощью цикла while:

companies = ["Microsoft", "Google", "Oracle", "Apple"] 
i = 0 
while i < len(companies): 
    print(companies[i]) 
    i += 1

# Microsoft 
# Google 
# Oracle 
# Apple 

#Для перебора с помощью функции len() получаем длину списка. С помощью счетчика i выводит по элементу, 
#пока значение счетчика не станет равно длине списка.


"=========================================Методы списков================================"

# Методы и функции по работе со списками
# Для управления элементами списки имеют целый ряд методов. Некоторые из них:

# append(item): добавляет элемент item в конец списка
# insert(index, item): добавляет элемент item в список по индексу index
# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
# clear(): удаление всех элементов из списка
# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError * pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
# count(item): возвращает количество вхождений элемента item в список
# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
# reverse(): расставляет все элементы в списке в обратном порядке
# Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

# len(list): возвращает длину списка
# sorted(list, [key]): возвращает отсортированный список
# min(list): возвращает наименьший элемент списка
# max(list): возвращает наибольший элемент списка


# append -метод, который добовляет элемент в конец списка
list1 = []
list1.append("hello")
list1.append(500)
list1.append([1, 2, 3])
print(list1) #["hello", 500, [1, 2, 3]]

# remove - метод, который удаляет елемент из списка по значению, но только первого вхождение в этого элемента, выдаст
# ошибку если такого элемента нет в списке.
list2 = [10, "hello", 500, "world", 1000, "hello", 500]
list2.remove("hello") 
print(list2) # [10, 500 ,"world", 1000, "hello", 500]

# pop - метод который удаляет элемент из списка по индексу. Если этого индекса нет ,выдаст ошибку Indexerror/

list3 = [10, 20, 30, 40, 50]
list3.pop() #удаление с конца
print(list3) #[10, 20, 30, 40]

list3.pop(1) # удаление по индексу 1
print(list3) # [10,30,40]

# также метод pop возвращает удаленный элемент      
list4 = [10, 20, 30, 40, 50]
popped = list4.pop(0) 
print(list4) # [20,30,40,50]
print(popped) # 10

# insert - метод, который добовляет элемент в список по индексу
list5 = [1, 2, 3, 4]
list5.insert(0, "hello")
print(list5)  # ["hello", 1, 2, 3, 4]


pop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pop.reverse())                   #первый способ перевернуть список        
print(pop[::-1])                       #второй способ
print(list(reversed(pop)))             #третий способ

# clear -чистит список 
pop =[1,2,3,4,5]
pop.clear() # []

# count - считает количество элементов в данной строке
pip = [11, 22, 11, 3, 2, 5]
print(pip.count(11))     # 2 


# index - показывает индекс данного элемента
list2 = ["hello", "world", "makers"]
ind = list2.index("hello")
print(ind)   # 0


# sort - сортирует по возврастанию
# если передать , то сортирует по убыванию


# copy -возвращает копию списка
list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

# extend - расширяет список другим списком
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.append(list2)
# list1  [1,2,3,4, [5,6,7,8]]

list1.extend(list2)
# list1  [1,2,3,4,5,6,7,8]
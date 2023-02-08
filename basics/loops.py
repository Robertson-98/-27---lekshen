"============================Циклы==========================="
# цикл - блок кода, который отрабатывается несколько раз
# for - цикл, который работает с итерируемыми обьектами, цикл заканчивает свою работу, когда он доходит до последнего элемента в итерируемом обьекте
# while - цикл, который работает до тех пор, пока условие верное

#---------------------------------------------------------------------------------------------
list1 = ["hello", 10, True, [1,2,3]]
for element in list1:
    print(element)
print(element)    # какой элемент был последний в цикле тот и сохраниться в переменной "element"



string1 = "hello world"
for letter in string1:
    print(letter)
#----------------------------------------------------------------------------------------------


i = 1
while i != 10:
    print("hello", i)
    i = i + 1   #  продублирует "hello" девять раз.

# i = 1
# while i: # 
#     print("hello world")
#     i = i + 1


"===================================Ключевые слова в циклах=================================="
#break - полность остонавливает цикл 
#continue -переход к следующей итерации 


for i in range(10):
    if i ==3:
        break
    print(i)
# 0
# 1
# 2



for i in range(10):
    if i == 3:
        continue
    print(i)
# 1,2,4,5,6,7,8,9


# с помощью метода remove удалите все единицы в списке
list1 = [ 1,2,3,1,2,4,5,9,1,1,5,7,7]
while 1 in list1:
    list1.remove(1)
print(list1)
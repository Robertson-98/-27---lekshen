##=======================3

# name_of_list = ['Hellomoiworld!']  
# string = name_of_list[0]

# len_ = len(string)

# if len_ % 2 == 0:
#     one = string[:len_ // 2]
#     sec = string[len_ // 2:]
# else:
#     one = string[:(len_ // 2) + 1]
#     sec = string[(len_ // 2) + 1:]

# new_list = list(sec) + list(one)
# print(new_list)

##=======================5

# suitcase = []
# suitcase.append("футболка")
# suitcase.append("шорты")
# suitcase.append("сланцы")
# suitcase.append("очки")
# suitcase.append("кепка")
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)


##=======================13

# x = input()
# list_ = x.split(",")
# list_.sort()
# print(list_)

##=======================15

# list_ = (list(range(55, 9181, 5)))
# print(list_)

##=======================18

# fio1 = input().split()[-1]
# fio2 = input().split()[-1]
# fio3 = input().split()[-1]
# fio4 = input().split()[-1]
# fio5 = input().split()[-1]

# lists = [fio1,fio2,fio3,fio4,fio5]
# lists.sort()
# print(lists)

##=======================19

# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# print(list_.count(number))

##=======================20

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# nums = []
# for element in list_:
#     if type(element) == int or element.isdigit():
#         nums.append(int(element))

# sum_ = 0

# for pop in nums:
#     sum_ = sum_ + pop
# print(sum_)


##=======================21

# str_list = ['abc', 'xyz', 'aba', '1221']
# pop1 = []
# for i in str_list:
#     if i[0] == i[-1]:
#         res = str_list.index(i)
#         pop1.append(res)
# print(pop1)

##=======================22

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lists.sort(key=len)

# if lists[0] == lists[-1]:
#     print(f"max_list {lists[-1]}")
#     print(f"min_list {None}")
# else: 
#     print(f"max_list {lists[-1]}")
#     print(f"min_list {lists[0]}")

##=======================23

# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []

# for i in range(step):
#     list1.append(list_[i::step])
# print(list1)

##=======================24

# size = 3 
# pop1 = []
# for i in range(size):
#     pop1.append([])
#     for j in range(1, size + 1):
#         pop1[i].append(j)
# print(pop1)
##=======================25

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# pop1 =input()
# pop2 = []
# for i in list_:
#     if i.startswith(pop1.lower()):
#         pop2.append(i)
# print(pop2)

##=======================26

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]

# pop1 = []
# pop2 = []

# for i in colors1:
#     if i not in colors2:
#         pop1.append(i)
# for i in colors2:
#     if i not in colors1:
#         pop2.append(i)
# print(pop1, pop2)

##=========================27

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# pop = []

# for pop1 in list1:
#     for pop2 in list2:
#         if pop1 == pop2:
#             pop.append(pop1)

# if len(pop) > 0:
#     print(True)
# else:
#     print(False)

##=========================28

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
# print(res)

##=========================29

# import itertools

# list_ = [1, 2, 3]
# pop1 = list(itertools.permutations(list_, len(list_)))

# for i in pop1:
#     print(i)

##==========================30

# K = 3
# pop1 = []
# for i in range(K):
#     pop1.append([])
#     for j in range(K):
#         pop1[i].append(0)
# print(pop1)

##==========================31

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# pop1 = []
# for i in colors:
#     pop1.append(i[::-1])
# print(sorted(pop1, key = len))

##==========================32

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'

# pop1 = []
# i = 0
# for pop2 in list_:
#     i += 1
#     pop1.append(pop2)
#     if i % step == 0:
#         pop1.append(element)

# print(pop1)

##==========================33

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# print(max(lists, key=sum))

##==========================34

# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for i in list_:
#     if list_.count(i) >1 and not i in repeated:
#         repeated.append(i)
# print(repeated)

##==========================35

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# pop1 = []
# pop2 = []
# for i in chars:
#     if i == merge_from:
#         pop2.append(i)

#     elif i == merge_to:
#         pop2.append(i)
#         pop1.append(''.join(pop2))
#         pop2 = []
#     elif pop2:
#         pop2.append(i)
#     else: 
#         pop1.append(i)
# print(pop1)

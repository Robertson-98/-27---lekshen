##=======================1

with open("task1.txt") as f:
    for line in f.readlines(9):
        print(line)

##=======================2

with open("task2.txt", "r") as f:
  for i in f.readlines():
    print(i)

##=======================3

with open("task3.txt", "a+") as f:
    f.write("0*1*2*3*4*5*6*7*8*9*")
    f.seek(0)
    print(f.read())

##=======================4

with open("task4.txt", "r") as f:
    print(len(f.readlines()))

##=======================5

with open("task5.txt", "r") as f:
    list_ = []
    ful = f.read() 
    for i in ful.split(): 
        list_.append(int(i)) 

with open("task6.txt", "a") as fw: 
    fw.write(f'{min(list_)}-{max(list_)}')

##======================6




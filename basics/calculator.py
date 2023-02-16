print("Ноль в качестве знака операции"
      "\nзавершит работу программы")

while True:
    try:
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
    except ValueError:
        print("Тут нужно вводить числа ")

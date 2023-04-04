'''
Дано натуральное число A > 1. Определите, каким по 
счету числом Фибоначчи оно является, то есть 
выведите такое число n, что φ(n)=A. Если А не 
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''


def Enter_user_num(msg):
    while True:
        user_num = input(msg)
        if user_num.isdigit() == False:
            print("Некорректный ввод значения.")
        elif int(user_num) <= 1:
            print("Введено число равное или меньше единицы. \n Повторите ввод")
        else:
            return user_num


def Rabbit_breeding(user_num):
    a = 0
    b = 1
    count = 0
    for i in range(int(user_num)):
        print(a)
        a = b
        b = a+b
        count = +1
        


user_num = Enter_user_num("Введите натуральное число больше единицы: ")
Rabbit_breeding(user_num)
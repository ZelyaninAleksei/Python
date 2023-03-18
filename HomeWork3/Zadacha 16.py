'''
Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
'''
import random


def Create_Array(msg):

    list_1 = list()
    x = int(input(msg))

    while True:
        y = input(
            "Заполнить массив автоматически случайными числами? \n Введите 1 - если да, 0 - если нет ")
        try:
            y = int(y)
            if y == 0:
                for i in range(int(x)):
                    print(f"Введите значение для элемента {i}")
                    n = int(input())
                    list_1.append(n)
                return list_1
            elif y == 1:
                for i in range(x):
                    list_1.append(random.randint(1, 10))
                return list_1
        except ValueError:
            print("Введены буквы, а не цифры. Повторите ввод ")


def FindNum(my_arroy):
    count = 0
    print("Введите значение элемента для поиска")
    x = int(input())
    for i in range(len(my_arroy)):
        if x == my_arroy[i]:
            count = count + 1
        i += 1
    return count


my_arroy = Create_Array('Введите количество элементов массива: ')
count = FindNum(my_arroy)
print(f" Созданный массив: \n {my_arroy}")
print(f" Искомое число встречается {count} раз(а) в текущем массиве")

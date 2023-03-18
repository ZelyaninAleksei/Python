'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

Ввод: 10
Ввод: 7
1 2 1 8 9 6 5 4 3 4
Вывод: 6
'''
import random


def Create_Array():
    while True:
        try:
            x = int(input("Введите размер массива -> "))
            list_1 = list()
            for i in range(x):
                list_1.append(random.randint(1, 10))
            return list_1
        except ValueError:
            print("Введены буквы, а не цифры. Повторите ввод ")


def Search_Close_Element(my_array, x):

    temp_x = abs(x - my_array[0])
    temp_index = 0
    for i in range(len(my_array)-1):

        if temp_x > abs(x - my_array[i+1]):
            temp_x = abs(x - my_array[i+1])
            temp_index = i + 1

        elif temp_x == abs(x - my_array[i+1]):
            if temp_x > my_array[i+1]:
                temp_x = my_array[i+1]
                temp_index = i+1
    return my_array[temp_index]


my_array = Create_Array()
print(f"Созданный массив {my_array}")
x = int(input("Введите значение поиска -> "))
minimal = Search_Close_Element(my_array, x)
print(f"Ближайший элемент к значению {x}: -> {minimal}  ")

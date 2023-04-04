# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
import random


def Create_new(msg):
    while True:
        try:
            array_size = int(input(f"Введите размер {msg} массива  -> "))
            my_list = list()
            for i in range(array_size):
                my_list.append(random.randint(1, 100))
            return my_list
        except ValueError:
            print("Введены знаки отличные от цифр. Повторите ввод.")


def Find(my_list, my_list2):
    list_diff = []
    for element in my_list:
        if element not in my_list2:
            list_diff.append(element)
    return list_diff


my_list = Create_new("первого")
my_list2 = Create_new("второго")
list_diff = Find(my_list, my_list2)

print(f" первый массив: \n {my_list}\n второй массив:\n {my_list2}")
print(f" элементы первого массива не входящие во второй: \n {list_diff}")

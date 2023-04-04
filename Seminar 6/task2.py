# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
import random

def Create_new__list():
    size = int(input("Введите размер массива -> "))
    list_1 = list()
    for i in range(size):
        list_1.append(random.randint(1, 10))
    return list_1


def Searh_element(new_list):
    final_list = []
    

new_list = Create_new__list()
print(f" Созданный массив: \n {new_list}")
'''
Дан список чисел. Определите, сколько в нем 
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения 
списка или список задан изначально.
'''

import random

def Create_Array():
    x = int(input("Введите размер массива -> "))
    list_1 = list()
    for i in range(x):
        list_1.append(random.randint(1, 10))
    return list_1

list_1 = Create_Array()
print(len(set(list_1)))       
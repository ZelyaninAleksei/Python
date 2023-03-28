#  Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

def create_list():
    
    array = list()
    size_array = int(input(" Введите размер массива: "))
    
    for i in range(size_array):
        array.append(random.randint(-20, 20))
    
    return array

def search_indexes_in_range(new_list):
    
    tmp = list()
    
    start_num = int(input(" Введите нижнюю границу диапазона: "))        
    finish_num = int(input(" Введите верхнюю границу диапазона: "))
    
    for i in range(len(new_list)):
        if new_list[i] >= start_num and new_list[i] <= finish_num:
             tmp.append(i)
    return tmp


new_list = create_list()

print(f" Созданый массив: \n {new_list}")
print(f"{search_indexes_in_range(new_list)} - индексы элементов в заданном диапазоне")
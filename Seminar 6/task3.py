# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
import random

def Create_new():
    while True:
        try:
            array_size = int(input(f"Введите размер массива  -> "))
            my_list = list()
            for i in range(array_size):
                my_list.append(random.randint(1, 10))
            return my_list
        except ValueError:
            print("Введены знаки отличные от цифр. Повторите ввод.")
            
def Find_pair(my_list):
    list.sort(my_list)
    var_find = input("Введите ")
            
my_list = Create_new()
print(f' Созданный массив \n {my_list}')
pair = Find_pair(my_list)
print(my_list)
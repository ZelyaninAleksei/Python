# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def enter_user_num(msg):

    tmp_val = int(input(f"Введите значение {msg}: "))
    return tmp_val


def сreate_Array(element, difference_of_elements, size):

    new_array = []
    
    for i in range(size):
        new_array.append(element)
        element += difference_of_elements
    return new_array


element = enter_user_num("начального элемента")
difference_of_elements = enter_user_num("шага")
size = enter_user_num("размера массива")

my_list = сreate_Array(element, difference_of_elements, size)

print(my_list)

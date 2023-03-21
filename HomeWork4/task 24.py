"""
    В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
    
 4 -> 1 2 3 4
9   
"""
import random


def entered_number_of_bushes():
    
    while True:
        number_of_bushes = input("Введите количество кустов: ")
        try:
            number_of_bushes = int(number_of_bushes)
            break
        except ValueError:
            print(
                "Похоже Вы ввели букву или иной знак отличный от цифры. Повторите ввод.")
    return number_of_bushes


def сrop_quantity(number_of_bushes):
    
    list_crop_quantity = list()
    y = int(input("Выберете способ заполнения уражайности кустов, предположим ягодами: \n 1 - заполнить случайными числами \n 2 - заполнить вручную \n"))
   
    while True:
        try:
            if y == 1:
                for i in range(number_of_bushes):
                    list_crop_quantity.append(random.randint(1, 10))
                    i = +1
                return list_crop_quantity
            elif y == 2:
                for i in range(number_of_bushes):
                    element = int(
                        input(f"Введите число урожая на кусте № {i+1}: "))
                    list_crop_quantity.append(element)
                return list_crop_quantity
        except ValueError:
            print(
                "Для заполнения урожайности необходимо вводить цифры. Повторите ввод.")


def search_and_harvest(crop_quan, number_of_bushes):
    
    max_sum = 0
    sum = 0
    
    for i in range(len(crop_quan)):
        
        if i == 0:
            sum = crop_quan[number_of_bushes-1] + crop_quan[i] + crop_quan[i+1]
        elif i == number_of_bushes-1:
            sum = crop_quan[i] + crop_quan[i-1] + crop_quan[0]
        else:
            sum = crop_quan[i] + crop_quan[i+1] + crop_quan[i-1]

        if sum > max_sum:
            max_sum = sum
    
    return max_sum


number_of_bushes = entered_number_of_bushes()
сrop_quan = сrop_quantity(number_of_bushes)
maximum_number_of_berries = search_and_harvest(сrop_quan, number_of_bushes)

print(f"Распределение урожая на кустах: \n {сrop_quan}")
print(
    f'Максимального числа ягод: {maximum_number_of_berries}')

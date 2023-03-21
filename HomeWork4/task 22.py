"""Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
"""
import random


def create_and_completion_set(msg):

    while True:
        x = input(f"Введите размер {msg} множества в пределах 20: ")
        try:
            x = int(x)
            if x > 20:
                continue
            break
        except ValueError:
            print(
                "Похоже Вы ввели букву или иной знак отличный от цифры. Повторите ввод.")

    while True:
        set_one = set()
        y = int(input(
            "Выберете способ заполнения множества: \n 1 - заполнить случайными числами \n 2 - заполнить вручную \n"))
        try:
            if y == 1:
                set_one = set(random.sample(range(1, 100), x))
                return set_one
            elif y == 2:
                for i in range(x):
                    element = int(input(f"Введите значение элемента {i+1}: "))
                    set_one.add(element)
                    i = +1
                return set_one
        except ValueError:
            print("Похоже, Вы ввели букву вместо варианта заполнения. Повторите ввод.")


set_one = create_and_completion_set("первого")
set_two = create_and_completion_set("второго")

result = sorted(list(set(set_one) & set(set_two)))

print(
    f" Заполненные множества: \n первое: \n {set_one} \n второе: \n {set_two} \n Элементы содержащиеся в двух множествах {result}")

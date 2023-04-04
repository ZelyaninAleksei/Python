# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# input 2 -> 3 4
# output 4 3

def super_recurse():    
    number = input()
    if number != '':
        super_recurse()
    print(number)

super_recurse()
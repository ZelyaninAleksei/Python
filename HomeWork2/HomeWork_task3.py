'''
 Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
'''

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

degree_of_number = int(input("Введите верхнюю границу: "))
i = 0
while (2**i)  <= degree_of_number:
    print(f" 2 в степени {i} = ",  2 ** i)
    i += 1

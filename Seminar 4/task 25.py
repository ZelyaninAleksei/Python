"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

text = input("Введите строку")
dict_letters = {}
text = text.split(" ")

for i in range(len(text)):
    if dict_letters.get(text[1]) == None:
        dict_letters[text[1]]=0
        
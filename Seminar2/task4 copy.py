 '''
 Иван Васильевич пришел на рынок и решил 
купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз 
потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9
'''
import random


days = input("Введите общее количество дней: ")
temperature = list()
temp = 0
resultTemp = 0

for i in range(int(days)):
    temperature.append(random.randint(-50, 50))
print(temperature)
for i in range(int(days)):
    if(int(temperature[i] > 0)):
        resultTemp += 1
    else:
        if(resultTemp > temp):
            temp = resultTemp
        resultTemp = 0
print(temp)
'''
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
'''
def Checking_entered_data():
    while True:
        number_bilets = input('Введите номер билета: ')
        if number_bilets.isdigit() == False:
            print("Введены буквы. Введите цифры.")
        elif len(number_bilets) < 6:
            print("Проверьте, все ли цифры Вы ввели.")
        elif len(number_bilets) > 6:
            print("Вы ввели больше шести цифр.")        
        else:
            return int (number_bilets)
        
def Happiness_check(number_bilets):
    summa1 =(number_bilets//100000) + (number_bilets%100000//10000)+(number_bilets%10000//1000)
    summa2 = (number_bilets%1000//100) + (number_bilets%100//10)+(number_bilets%10)
    print(f"Сумма 1 = {summa1}")
    print(f"Сумма 2 = {summa2}")
    if summa1 == summa2:
        print("Ура! Счастливый билет! Можно съесть )")
    else: print("К сожалению, простой билет! Повезёт в следующий раз!")

number_bilets = Checking_entered_data()
Happiness_check(number_bilets)
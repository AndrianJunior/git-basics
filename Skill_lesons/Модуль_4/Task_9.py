print('Задача 9. Плохой циферблат')

# У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега,
# но он постоянно глючит и сбрасывается.
# Саша заметил закономерность:
# каждый раз, когда сумма цифр на циферблате превышает число текущего дня,
# циферблат сбрасывается.

# Напишите программу,
# которая получает на вход от пользователя два числа: пробег и номер дня (первое — обязательно трёхзначное),
# затем находит сумму цифр первого числа,
# и если эта сумма больше второго числа,
# выводит сообщение: «Сброс», — и сбрасывает пробег до нуля.
# В противном случае выводится: «Сегодня не сломался».
# В конце также выводится сам пробег.
probeg = int(input("Введите пробег:"))
day = int(input("Введите число сегодняшнее:"))
num_1 = probeg // 100
#print(num_1)
num_2 = probeg % 100 // 10
#print(num_2)
num_3 = probeg % 100 % 10
#print(num_3)
summa = num_1 + num_2 + num_3
#print(summa)
if summa > day:
    print("Сброс!")
else:
    print("Сегодня не сломался!")
print(probeg, "Km")

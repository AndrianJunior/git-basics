print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
a = int(input("Введите первое число(от):"))
b = int(input("Введите второе число(до):"))
if a < b:
    for i in range(a,b):
        if i % 3 == 0:
            print(i)
else:
    for i in range(b,a):
        if i % 3 == 0:
            print(i)

print('Задача 1. Календарь')

# Мы продолжаем разрабатывать удобный календарь для смартфона.
# Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
#
# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
#
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2

day_weeks = str(input("Введите день недели:"))
#days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
count=0
for num_day in "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье":
        count+=1
        if day_weeks == num_day:
                print("Номер дня недели:",count)





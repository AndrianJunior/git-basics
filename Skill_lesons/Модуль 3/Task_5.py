print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.
minute = int(input("Введите количество минут:"))
count = minute // 60
count_2 = minute % 60
print(count, "час", count_2, "минут")

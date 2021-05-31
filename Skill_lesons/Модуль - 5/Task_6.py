print('Задача 6. Защита от дурака')

# Мы участвуем в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел,
# и нам необходимо написать этакую «защиту от дурака».
#
#
# Напишите программу,
# которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными.
# Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.
number = int(input("Введите число:"))
if number > 9 and number <= 99 or number < -9 and number >= -99:
    print("Число двузначное")
else:
    print("Число не двузначное")
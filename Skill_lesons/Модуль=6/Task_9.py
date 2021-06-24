print('Задача 9. Игра «Угадай число»')

# В одном из домашних заданий мы делали задачу,
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том,
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число.
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.

# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4
number = 13
running = True
i = 0
while running:
    i = i + 1
    guess = int(input("Введите целое число : "))
    count =+ 1
    if guess == number :
        print("Поздравляю, вы угадали.")
        running = False
    elif guess < number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
print("Число попыток:", i)
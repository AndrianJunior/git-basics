print('Задача 7. Поездка по кругу')

# Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
# Длина дороги — 115 километров.
# Вася стартует с нулевого километра и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?
#
# Реализуйте программу,
# которая спрашивает у пользователя v и t,
# и выводит целое число от 0 до 114 — номер километра, на котором остановится Вася.
# Учтите, что он может прокатиться больше одного круга.
road_dist = 115
speed = int(input("Введите среднюю скорость(km/h):"))
time = int(input("Введите время(hour):"))
# time_convert = time * 60
# print(time_convert)
count = time * speed // 115
count_2 = time * speed % 115
print("Василий остановился на", count,"кругу",count_2, "Км.")
# Длина круга 115 км, когда проедем 114 км — будет не хватать одного километра до конца круга,
# попробуйте ввести 2, 57. При использовании оператора взятия остатка от деления
# мы не можем получить число, превышающее или равное. То есть для N % 2 можем
# получить 0, если число делится на 2 или 1. Для N % 4 — 0, 1, 2, 3.

print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
#
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.
env = 12
letter = int(input("Введите значение одной стороны письма: "))
fold = 0
while env <= letter:
    letter /= 2
    fold += 2
print("Нужно ", fold, "раза сложить письмо пополам")
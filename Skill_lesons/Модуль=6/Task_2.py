print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
debtor = input("Введите имя должника:")
debt = int(input("Введите сумму долга:"))
money = 0
while debt > money :
 print(debtor ,"ваша задолженность составляет",debt )
 money_deb = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?"))
 money = money_deb
 if money < debt:
  print("Маловато,",debtor,". Давайте ещё раз.")
print("Отлично,",debtor,"! Вы погасили долг. Спасибо!")
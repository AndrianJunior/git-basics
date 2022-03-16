print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))
x = int(input("Введите число х: "))
numerator = 1
denominator = 1
for deductible in range(1,6+1):
  numerator *= x - ((2 ** deductible) - 1)
  denominator *= x - (2 ** deductible)
z = numerator / denominator
print("Выражение будет равно = ", z)
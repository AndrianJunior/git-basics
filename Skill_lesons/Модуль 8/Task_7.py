print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant, expenses = 10000, 12000
months = 10
inflation = 1.03
total_expenses = expenses
for i in range(2, 11):
    expenses = expenses * inflation
    total_expenses += expenses
parents_money = total_expenses - educational_grant * months
print("Студенту надо попросить",round(parents_money, 2), "рублей")
#крутая задача я её помню ещё из старого курса .

print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.
student_3 = 0
student_4 = 0
student_5 = 0
students = int(input("Введите количество студентов:"))
for i in range(1, students + 1):
    grades = int(input("Введите оценку " + str(i) + " студента:"))
    if grades == 3:
        student_3 += 1
    elif grades == 4:
        student_4 += 1
    elif grades == 5:
        student_5 += 1
if student_3 > student_5 and student_4 < student_3:
    print("Сегодня больше троечников.")
elif student_4 > student_3 and student_4 > student_5:
    print("Сегодня больше хорошистов")
elif student_5 > student_4 and student_5 > student_3:
    print("Сегодня больше отличников")
print(student_3)
print(student_4)
print(student_5)

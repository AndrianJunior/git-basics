print ("Hello world")
number = 23
running = True

while running:
    guess = int(input("Введите целое число : ")) #guess -угадай ,отгадай

    if guess == number :
        print("'Поздравляю, вы угадали.'")
        running = False  # это останавливает цикл while
    elif guess < number:
        print("'Нет, загаданное число немного больше этого'")
    else:
        print("'Нет, загаданное число немного меньше этого.'")
else:
    print("'Цикл while закончен.'")
    # Здесь можете выполнить всё что вам ещё нужно

#True и False называются булевым типом данных,
#и вы можете считать их эквивалентными значениям 1 и 0 соответственно.
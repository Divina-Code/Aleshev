isGuessed = False

while isGuessed != True:
    puzzle = "\nБыло 2 козла, сколько? \nНа размышление дается 30 секунд"
    answer = input(puzzle)
    if answer == "2":
        print('Есть пробитие!')
        isGuessed = True
    elif answer == "снюс":
        print("Шайбу карге!")
    else:
        print("Пробуй еще")
    print("пасибо за игру")
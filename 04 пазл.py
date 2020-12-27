isGuessed = False

while isGuessed != True:
    puzzle = "\nБыло 2 козла, сколько? \nНа размышление дается 30 секунд"
    answer = input(puzzle)
    if answer == "2":
        print('Пойман за руку как дешевка.')
    elif answer == "шайбу карге":
        print("Правильно!")
    else:
        print("Пробуй еще")
    print("пасибо за игру")
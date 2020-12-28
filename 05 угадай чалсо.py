
number1 = int(228)
chislo = False
while chislo != True:
    number =int(input('Введите ваше число'))
    if number == number1:
        chislo = True
        print('Правильно!')
    elif number > number1:
        print('Меньше!')
        chislo = False
    elif number < number1:
        print('Больше!')
        chislo = False
    else:
        chislo =False
        print('Пробуй еще!')
print('Списание со счета: 10000 рублей')
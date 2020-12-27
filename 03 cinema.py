name = input('Укажите свое имя')
born= int(input('Укажите свой год рождения'))
years_old = 2020 - born
if years_old < 18:
    print('Предлагаем вам посмотреть комедию.')
else:
    print('Предлагаем вам посмотреть боевик.')
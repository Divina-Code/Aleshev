print('Hello, user!')
user_name = input("What is ur name?")
print('Hello', user_name, "in ur name", len(user_name), 'letters')
user_year = int(input('When u was born?'))
if len(str(user_year)) == 4:
    print("nice year", user_year)
    print(2020-user_year)
else:
    print("U make a little mistake")
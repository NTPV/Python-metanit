try:
    input = input('''Привет!
    ..это многострочная строка
Введите число: ''')
    intinput = int(input)
    print(f'''Вы ввели число: 
{intinput}
Конец строки''')
except:
    print('''Возникла ошибка''')

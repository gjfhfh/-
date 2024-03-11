# Python

with open('space.txt', 'r', encoding='utf-8') as f:
    a = []
    for i in f:
        a.append(i.strip())  # Записываем данные файла в список а
    a0 = a[0] + '*password' # Записываем первый элемент списка в отдельную переменную и добаляем столбец пароля
    a = a[1:]  # Убираем первый элемент списка, так как там нет названий кораблей и т.п.

with open('space_uniq_password.csv', 'w', encoding='utf-8') as f:
    print(a0, file=f)
    for i in a:
        # Создаем пароль
        psw = ''.join(list(i.split('*')[1][-3:].upper()) + list(i.split('*')[0].split('-')[0][
                                                                len(i.split('*')[0].split('-')[0]) // 2 - 1:len(
                                                                    i.split('*')[0].split('-')[0]) // 2 + 1][
                                                                ::-1]) + list(i.split('*')[1][:3].upper()[::-1]))
        print(i+'*'+psw,file=f) # Созданный пароль записываем в новый файл с остальными данными
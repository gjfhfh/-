# Python

with open('space.txt', 'r', encoding='utf-8') as f:
    a = []
    for i in f:
        a.append(i.strip())  # Записываем данные файла в список а
    a0 = a[0]
    a = a[1:]  # Убираем первый элемент массива, так как там нет названий кораблей и т.п.

with open('space_new.txt', 'w', encoding='utf-8') as f:
    print(a0, file=f)
    for i in a:
        if '0 0' not in i.split('*')[2]:
            print(i, file=f)
        else:
            n = int(i.split('*')[0].split('-')[-1][0])
            m = int(i.split('*')[0].split('-')[-1][1])
            t = len(i.split('*')[1])
            x_d, y_d = i.split('*')[-1].split()
            if n > 5:
                x = n + int(x_d)
            else:
                x = (n + int(x_d)) * (-4) + t
            if m > 3:
                y = m + t + int(y_d)
            else:
                y = (n + int(y_d)) * m * (-1)
            q = ''.join(i.split('*')[0]) + '*' + ''.join(i.split('*')[1]) + '*' + f'{x} {y}' + '*' + ''.join(
                i.split('*')[3])
            print(q, file=f)

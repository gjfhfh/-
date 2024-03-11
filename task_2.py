# Python

with open('space.txt', 'r', encoding='utf-8') as f:
    a = []
    for i in f:
        a.append(i.strip())  # Записываем данные файла в список а
    a = a[1:]  # Убираем первый элемент массива, так как там нет названий кораблей и т.п.
    for i in range(len(a)):  # Делаем сортировку
        for j in range(i + 1, len(a)):
            if int(a[i].split()[0].split('*')[0].split('-')[-1]) > int(a[j].split()[0].split('*')[0].split('-')[-1]):
                a[i], a[j] = a[j], a[i]
k = 0
with open('spaceship_names.txt', 'w', encoding='utf-8') as f:
    for i in a:
        print(i, file=f) # Записываем в новый файл первые 10 кораблей
        k += 1
        if k == 10:
            break

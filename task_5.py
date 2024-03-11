# Python

def f1(a):  # хэш функция
    d = {}
    for i in a:
        if i.split('*')[1] in d.keys():
            d[i.split('*')[1]] += [i.split('*')[0]]
        else:
            d[i.split('*')[1]] = [i.split('*')[0]]
    return d


with open('space.txt', 'r', encoding='utf-8') as f:
    a = []
    for i in f:
        a.append(i.strip())  # Записываем данные файла в список а
    a = a[1:]  # Убираем первый элемент массива, так как там нет названий кораблей и т.п.

k = 0
with open('ship_info.txt', 'w', encoding='utf-8') as f:
    d1 = f1(a)
    for i in d1.keys():
        if k >= 10:
            break
        print(f'{i}: {d1[i]}', file=f) # Записываем в файл первые 10 планет
        k += len(d1[i])
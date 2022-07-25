# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


def Unique(n):
    x = 0
    a = list(n.split())
    b = []
    i = 0
    while i < len(a):
        x = a[i]
        c = 0
        for j in range(len(a)):
            if int(a[j]) == int(x):
                c += 1
        if c < 2:
            b.append(int(x))
        i += 1
    return b


num = input('Введите числа: ')
print(f'Список неповторяющихся элементов: {Unique(num)}')
# 4. Задана натуральная степень k.Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.


import random


def Polynomial(k):
    s = ''
    r = 0
    for i in range(k, 0, -1):
        r = random.randint(0, 100)
        if r == 0:
            s += ''
        elif r == 1:
            s += str(f'x^{i} + ')
        elif i != 1:
            s += str(f'{r}x^{i} + ')
        else:
            s += str(f'{r}x ')
    r = random.randint(0, 100)
    if r != 0:
        s += str(f'+ {r} = 0')
    else:
        s += str(f'= 0')
    return s


k = int(input("Введите степень: "))
while k <= 0:
    k = int(input("Введите число больше 0: "))
print(Polynomial(k))
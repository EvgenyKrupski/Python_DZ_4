# 2. Задайте натуральное число N. Напишите программу, которая составит список простых делителей
# числа N. (1 - составное число)


def Dividers(n):
    a = []
    i = 2
    while i <= n:
        if n % i == 0:
            c = 0
            j = 2
            while j < i:
                if i % j == 0:
                    c += 1
                j += 1
            if c == 0:
                a.append(i)
        i += 1
    return a


n = int(input("Введите число: "))
print(Dividers(n))
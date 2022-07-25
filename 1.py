# # Вычислить число c заданной точностью d
# # Пример:
# # при d = 3, π = 3.141

def Pi(n):
    i = 1
    x = 3
    g = 1
    p = 12**0.5
    s = ''
    while i < 10000:
        if i % 2 != 0:
            g = g - (1/(x*(3**i)))
        else:
            g = g + (1/(x*(3**i)))
        x += 2
        i += 1
    p *= g
    p = str(p)
    for i in range(n+2):
        s += str(p[i])
    return float(s)


d = int(input("Введите ваше число: "))
while d < 1 or d > 15:
    d = int(input("Введите число больше чем 0 и меньше чем 16: "))
print(Pi(d))
from decimal import *
from math import factorial

def pi(n):
    pi = Decimal(0)
    for i in range(n):
        pi += pow(Decimal(-1), i) * (Decimal(factorial(6 * i)) * (13591409 + 545140134 * i) / (pow(640320, (3 * i)) * (pow(factorial(i), 3) * (factorial(3 * i)))))
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pow(pi, -1)
    return pi

n = int(input("Введите количество знаков после запятой в числе pi: "))
getcontext().prec = n+1
print(pi(n))

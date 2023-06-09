# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# python Task_12.py

import math
import os
os.system('cls')

X = int(input("Задумайте число X: "))
Y = int(input("Задумайте число Y: "))

S = 0
p = 0

while 0 < X and Y < 1000:
    s = X + Y
    p = X * Y
    print(f"Петя дал подсказку: S = {s}, P = {p}")
    
    if s * s < 4 * p:
        print('Нет корней')
    else:
        x = (s + math.sqrt(s * s - 4 * p)) / 2
        y = (s - math.sqrt(s * s - 4 * p)) / 2
    print(x)
    print(Y)
    break







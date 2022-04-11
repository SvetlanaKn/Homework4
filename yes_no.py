"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(s: list):
    s2 = []
    for i in s:
        if s2.count(i) > 0:
            print('YES')
        else:
            s2.append(i)
            print('NO')

s = [1,3,4,3,4,2,3,4,5,6,8,7,0,0]
yes_or_no(s)

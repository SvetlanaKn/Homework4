"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.
Можно пользоваться только функциями, операторами и условиями.
"""

def sum_of_numbers(abs: str):
    s = 0
    for i in abs:
        s += int(i)
    return s
print(sum_of_numbers(12))


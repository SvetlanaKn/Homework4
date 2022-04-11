"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.
Можно пользоваться только функциями, операторами и условиями.
"""

def sum_of_numbers(n: str, s=0):
    if s == len(n):
        return(0)
    else:
        return sum_of_numbers(n, s + 1) + int(n[s])
n = 12
print(sum_of_numbers(str(n)))
s = sum(list(str(n)))

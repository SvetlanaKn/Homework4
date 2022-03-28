# -*- coding: utf-8 -*-
number_one = float(input("Enter first number =  "))
operation = input("Enter operation(*, /, +, -) =  ")
number_two = float(input("Enter second number =  "))
result = r'print({} {} {})'.format(number_one, operation, number_two)
exec(result)
print()

print('������������ ��� � ������������ Python')
print("��� ���������� 'stop' � ������ operation")

while True:
    count = 0
    operation = input("Enter operation(*, /, +, -) =  ")
    if operation == 'stop':
        break
    if operation not in ('*', '/', '+', '-'):
        print("������� ��������� ����")
        continue
    try:
        number_one = float(input("Enter first number =  "))
        number_two = float(input("Enter second number =  "))
        if operation == "+":
            print('Equal =', number_one + number_two)
            count += 1
        elif operation == "-":
            count += 1
            print('Equal =', number_one - number_two)
        elif operation == "*":
            count += 1
            print('Equal =', number_one * number_two)
        elif operation == "/":
            count += 1
            if number_two != 0:
                print('Equal =', number_one / number_two)
            else:
                print("������� �� ����!")
            print(count)
        print(count)
    except NameError:
        print("������������ ��� ������")
    except IndentationError:
        print("������������ ��� ������")
    except TypeError:
        print("������������ ��� ������")
    except ValueError:
        print("������������ ��� ������")
    finally:
        print("����� �������")
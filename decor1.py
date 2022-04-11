"""
С помощью декораторов реализовать конвейер сборки бургера
Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"
Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"
Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"
Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"
Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"
Написать функцию beef, которая:
 - печатает "### говядина ###"
Написать функцию chicken, которая:
 - печатает "|||| курица ||||"
1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка
2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

def bread(func):
    def wrapper(*args, **kwargs):
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs):
        print("~~~~ салат ~~~~~")
        func()
    return wrapper

def cheese(func):
    def wrapper(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapper

def addictive(func):
    def wrapper(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        func()
        print("*** помидоры ****")
    return wrapper

def beef(func):
    def wrapper(*args, **kwargs):
        print("### говядина ###")
        func()
    return wrapper

def chickeen(func):
    def wrapper(*args, **kwargs):
        print("|||| курица ||||")
        func()
    return wrapper

@bread
@addictive
@beef
def hamburger(*args, **kwargs):
    return(hamburger)

hamburger()


print('-----------------*****************------------------')


@bread
@cheese
@salad
@chickeen
def sandwich(*args, **kwargs):
    return(sandwich)

sandwich()
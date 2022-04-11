"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}
например: {
    'p': 2,
    'y': 1,
    ...
}
Нельзя пользоваться collections.Counter!
"""
# def count_char(STR_VAL: str):
#     res = {}
#     for i in STR_VAL:
#         if i in res.keys():
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res

def count_char(STR_VAL: str):
    h = set(STR_VAL)
    return{i:STR_VAL.count(i) for i in h}

print(count_char(STR_VAL = 'python is the fastest-growing major programming language'))
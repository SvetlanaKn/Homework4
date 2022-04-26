# """
# Создать класс User с атрибутами:
# Свойства:
# 	- name - имя - содержит только буквы русского алфавита
# 	- login - логин - может содержать  только латинские буквы цифры и черту
# 	подчеркивания быть не менее 6 символов
# 	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия:
# 					содержит менее шести символов
# 					содержит строчную букву
# 					содержит заглавную букву
# 					содержит число
# 	- is_blocked - заблокирован
# 	- subscription_date - дата до какой действует подписка
# 	- subscription_mode - вид подписки (free, paid)
# Методы:
# 	- bloc - принимает логическое значение и помечает пользователя заблокированным
# 	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату.
# 						Если дата не передана значит на дату проверки.
# 						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
# 	- change_pass - смена пароля и присваивание его в качестве действующего.
# 						Пароль должен пройти валидацию.
# 						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
# 	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.
# Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного -
# пароль. Логин и пароль должны быть проверен на валидность.
# Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть
# выведен на экран(консоль).
# При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
# При изменении даты подписки  вид подписки меняется на платный.
# """

from datetime import date, timedelta, time
import re
import random
import time


class User:
    __name: str
    __login: str
    __password: str
    is_blocked: bool
    subscription_date: date
    subscription_mode: str

    def __init__(self, __name, __login, __password='', is_blocked=False, subscription_date=None, subscription_mode='free'):

        while not self.__check__name(__name):
            __name = input("Введите новое имя пользователя")
            self.__check__name(__name)
            self.__name = __name
            break
        else:
            self.__name = __name

        while not self.__check__login(__name, __login):
            __login = input("Введите новый логин пользователю: ")
            self.__check__login(__login, __name)
            self.__login = __login
            break
        else:
            self.__login = __login

        self.__password = self.__check_password(__password)
        self.is_blocked = is_blocked
        self.subscription_mode = subscription_mode

        if subscription_date is None:
            self.subscription_date = date.today() + timedelta(days=30)
        else:
            self.subscription_date = subscription_date

    def get_info(self):
        if self.is_blocked:
            print(f'Извините, {self.__name} заблокирован')
        else:
            print(
                f'name: {self.__name}\nlogin: {self.__login}\nsub_date: {self.subscription_date}\nSub_mode: {self.subscription_mode}\n')

    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False

    def __check__name(self, __name):
        if len(re.findall("[а-яА-Я]", __name)) == len(__name):
            return True
        else:
            print(f'{__name} - Измените имя!')
            return False

    def __check__login(self, __login, __name):
        if re.match(r'^[A-Za-z0-9_]{6,}$', __login):
            return True
        else:
            print(f'{__login} - Поменяйте Ваш логин!')
            return False

    def __check_password(self, __password):
        if self.__check_password_change(__password):
            return __password
        else:
            __password = ''
            __password = self.__change_pass(__password)
            return __password

    def __check_password_change(self, __password):
        if re.search(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z_-]{6,}$', __password):
            return True
        else:
            return False

    def __change_pass(self, __password):
        if self.__check_password_change(__password):
            print('Вы успешно сменили пароль.')
            return ''
        else:
            print(f'{self.__name} - Пароль небезопасен. Пароль будет сгенерирован системой.')
            time.sleep(1)
        while not self.__check_password_change(__password):
            s1 = '1234567890'
            s2 = 'qwertyuiopasdfghjklzxcvbnm'
            s3 = s2.upper()
            s4 = s1 + s2 + s3
            j = list(s4)
            new_password = ''
            for x in range(10):
                new_password = new_password + random.choice(j)
            __password = new_password
        print(f'{self.__name} - вот Ваш новый пароль, сохраните и запомните его: {__password}\n')
        return __password

    def check_subscr(self):

        if self.subscription_date <= date.today():
            print(f'{self.__name} - пополните счет, подписка закончилась')
        else:
            data = self.subscription_date - date.today()
            print(f'{self.__name} У вас осталось {data.days} дней подписки, вид подписки: {self.subscription_mode}')

    def donate(self, val: int):
        self.subscription_mode = 'paid'
        self.subscription_date += timedelta(days=val)


user1 = User('Команда', 'weryui8')
user2 = User('Туманы', 'hjgdsf', '2022mnbvc')
user3 = User('Воздух', 'fghkgkh', 'kjgffTY78')
user4 = User('Праздник', 'fgd_jks', 'lkjggYTRR4')

user1.get_info()
user2.get_info()
user2.block()
user2.get_info()
user2.unblock()
user2.get_info()

date1 = date(2022, 4, 13)
date2 = date(2022, 8, 19)
date3 = date(2022, 1, 25)
data4 = date(2022, 3, 30)
user1.check_subscr()
user2.subscription_date = data4
user2.check_subscr()
user1.get_info()
user1.donate(3)

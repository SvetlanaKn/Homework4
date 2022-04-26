# """
# Создать класс MobilePhone на основе класса Phone из пред ДЗ, у которого будут следующие атрибуты:
# добавить свойства:
# 	is_busy - занято - когда кто-то позвонил до момента когда положили трубку должен иметь значение True
# переопределить методы:
# 	- receive_call - теперь не только выводит фразу с именем но и сохраняет время и имя в историю.
# 						Если в момент вызова трубка еще не положена - вернуть "занято".
# добавить методы:
# 		- receive_sms - принимает имя и текст и сохраняет в историю
# 		- call_history - возвращает историю звонивших с датой и временем именем и случайным номером
# 		телефона формата +375*********
# 		- sms_history - возвращает историю sms (имя/дата/время/текст)
# 		- сделать метод (положил трубку)
# 		* метод receive_call принимает номер и если есть в справочнике в историю записать имя
# 		* положить трубку с возвратом  времени разговора которое тоже в записывается историю
# from datetime import date
#
# CURRENT_YEAR = date.today().year
# """
import datetime
import time


# import random


class MobilePhones:
    brand: str
    model: str
    issue_year: str
    call_history: list
    is_busy: bool
    miss_call: list
    incoming_sms: list
    start_call: time

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.call_history = []
        self.is_busy = False
        self.miss_call = []
        self.incoming_sms = []
        self.start_call = 0

    def __str__(self):
        return f"\n Бренд: {self.brand} \nМодель: {self.model} \nГод выпуска: {self.issue_year}\n" \
               f"\n История пропущенных звонков: {str(self.miss_history)}" \
               f"\n История звонков: {str(self.call_history)}"

    def receive_call(self, name, tel_number):
        if not self.is_busy:
            self.is_busy = True
            self.start_call = datetime.datetime.now()
            print(f'\nЗвонит {name}\n')
            self.call_history.append([self.start_call.strftime("%d/%m/%Y %H.%M.%S"), name, tel_number])
        else:
            print("Занято")
            self.miss_call.append([self.start_call.strftime("%d/%m/%Y %H.%M.%S"), name, tel_number])
            self.call_history.append([self.start_call.strftime("%d/%m/%Y %H.%M.%S"), name.center(10), tel_number])

    def calls_history(self):
        print('\nИстория звонков:')
        for i in self.call_history:
            print(i)

    def end_call(self):
        self.is_busy = True
        print("Звонок завершен.")
        self.start_call = 0

    def miss_history(self):
        for i in self.miss_call:
            print("История пропущенных звонков:", i)

    def get_info(self):
        return f"Бренд: {self.brand}, Модель: {self.model}, Год выпуска: {self.issue_year}, {self.call_history}"

    def sms_receive(self, name, text):
        self.incoming_sms.append([name, text])
        print(f'Новое смс от {name}, {text}', self.start_call.strftime("%d/%m/%Y %H.%M.%S"))

    def sms_history(self, name, text):
        for i in self.incoming_sms:
            print(f"SMS {name}, {text}", self.start_call.strftime("%d/%m/%Y %H.%M.%S"))


x = MobilePhones("Samsung", 'A51', 2021)
name1 = "Aleksandr"
name2 = "Max"
name3 = "Gleb"
name4 = "Evgenia"
txt = 'Hello'
x.receive_call(name1, "+37546678687675")
time.sleep(2)
x.receive_call(name2, "+3754657895799")
time.sleep(1)
x.receive_call(name3, "+3754632789000")
time.sleep(1)
x.receive_call(name4, "+3754632789789")
x.end_call()

x.miss_history()

x.calls_history()
x.sms_history(name1, txt)

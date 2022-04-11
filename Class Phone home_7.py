# """
# Создать класс Phone, у которого будут следующие атрибуты:
# Определить атрибуты:
# - brand - бренд
# - model - модель
# - issue_year - год выпуска
# Определить методы:
# - инициализатор __init__
# - receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
# - get_info, который будет возвращать кортеж (brand, model, issue_year)
# - метод __str__, который выводит на экран информацию об устройстве:
# Бренд: {}
# Модель: {}
# Год выпуска: {}
# """

class Phones:

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self. model = model
        self.issue_year = issue_year

    def __call__(self, name):
        return f"Звонит {name}"


    def get_info(self):
        print(f"Бренд: {self.brand}\n"
              f"Модель: {self.model}\n"
              f"Год выпуска: {self.issue_year}\n"
              )

    def __str__(self):
        return f"{self.get_info()}"

phone = Phones("Samsung", 'A51', 2021)

phone.get_info()
str(phone)


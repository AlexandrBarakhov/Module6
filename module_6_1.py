"""
Ваша задача:
Создать родительский(базовый) класс Car, который имеет свойство price = 1000000 и метод def horse_powers,
который возвращает количество лошадиных сил для автомобиля.
Создать наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите метод horse_powers
Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
а также переопределите метод horse_powers
"""


class Car:
    """Базовый класс для автомобилей."""
    price = 1_000_000  # Цена по умолчанию

    def horse_powers(self):
        """Возвращает количество лошадиных сил."""
        return "Вывод лошадиных должен быть определен в дочернем классе"


class Nissan(Car):
    """Класс для автомобилей Nissan, наследующий от Car."""

    price = 1_200_000  # Цена для Nissan

    def horse_powers(self):
        """Возвращает количество лошадиных сил для Nissan."""
        return 150


class Kia(Car):
    """Класс для автомобилей Kia, наследующий от Car."""

    price = 900_000  # Цена для Kia

    def horse_powers(self):
        """Возвращает количество лошадиных сил для Kia."""
        return 120


# Пример использования:
car = Car()
nissan = Nissan()
kia = Kia()

print(f"Цена автомобиля Car: {car.price}")
print(f"Лошадиные силы Car: {car.horse_powers()}")

print(f"Цена автомобиля Nissan: {nissan.price}")
print(f"Лошадиные силы Nissan: {nissan.horse_powers()}")

print(f"Цена автомобиля Kia: {kia.price}")
print(f"Лошадиные силы Kia: {kia.horse_powers()}")

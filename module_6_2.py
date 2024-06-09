"""
Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
которая возвращает количество лошадиных сил для автомобиля
Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
а также переопределите функцию horse_powers
Создайте экземпляр класса Nissan и распечатайте через функцию print vehicle_type, price

"""


class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1_000_000

    def horse_powers(self):
        return "Неизвестно"


class Nissan(Car, Vehicle):
    vehicle_type = "Nissan"
    price = 1_500_000

    def horse_powers(self):
        return 200


nissan = Nissan()

print(f"Тип транспортного средства: {nissan.vehicle_type}\nЦена: {nissan.price}")
# print(f"Лошадиные силы: {nissan.horse_powers()}")

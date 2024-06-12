from math import pi, sqrt


class Figure:
    '''
    Класс описывает фигуру
    '''

    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False  # закрашенность

    # Геттер для цвета
    def get_color(self):
        return list(self.__color)

    @staticmethod
    def __is_valid_color(r, g, b):
        return (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255)

    # Сеттер для цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)

    # Геттер для закрашенности
    def is_filled(self):
        return self.filled

    # Сеттер для закрашенности
    def set_filled(self, filled):
        if isinstance(filled, bool):
            self.filled = filled

    def get_sides(self):
        return list(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)  # сюда передается длина окружности (периметр окружности)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.calculate_height(0)  # Вычисляем высоту относительно первой стороны по умолчанию

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height

    def get_height(self):
        return self.__height

    def calculate_height(self, side_index):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        # Используем правильную сторону для вычисления высоты
        return 2 * sqrt(s * (s - a) * (s - b) * (s - c)) / self.get_sides()[side_index]

    def get_height_by_side(self, side_index):  # Возвращает высоту треугольника относительно заданной стороны

        if 0 <= side_index < 3:
            return self.calculate_height(side_index)
        else:
            raise ValueError("Неверный индекс стороны")


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    cube1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    circle1.set_sides(15)  # Изменится
    print(cube1.get_sides())
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    #####
    print()
    triangle1 = Triangle((100, 200, 300), 2, 3, 4)
    print(triangle1.get_sides())
    print(triangle1.get_height())  # Высота относительно первой стороны (длиной 2)
    print(triangle1.get_height_by_side(1))  # Высота относительно второй стороны (длиной 3)
    print(triangle1.get_height_by_side(2))  # Высота относительно третьей стороны (длиной 4)
    # Проверка начального состояния закрашенности (по умолчанию False)
    print(triangle1.is_filled())  # Вывод: False
    # Установка закрашенности
    triangle1.set_filled(True)
    # Проверка состояния закрашенности после установки
    print(triangle1.is_filled())  # Вывод: True

from abc import ABC, abstractmethod


class ComputerColor:
    """
    Напишите абстрактный класс ComputerColor:
    ● Имеет абстрактный метод __repr__
    ● Имеет абстрактный методы __mul__ и __rmul__
    ● Класс Color наследуются от ComputerColor
    """
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass


class Color(ComputerColor):
    """
    Класс Color, который выводит ● в заданном цвете RGB
    """
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_level, green_level, blue_level):
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self):
        return f'{self.START};{self.red_level};{self.green_level};{self.blue_level}{self.MOD}●{self.END}{self.MOD}'

    def __repr__(self):
        return f'{self.START};{self.red_level};{self.green_level};{self.blue_level}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, another):
        """
        Возможность сравнивать цвета
        """
        eq_red = (self.red_level == another.red_level)
        eq_green = (self.green_level == another.green_level)
        eq_blue = (self.blue_level == another.blue_level)
        return eq_red and eq_green and eq_blue

    def __add__(self, another):
        """
        Cмешивание цветов через сложение экземпляров класса Color
        """
        new_color = Color(
            (self.red_level + another.red_level),
            (self.green_level + another.green_level),
            (self.blue_level + another.blue_level)
        )
        return new_color

    def __hash__(self):
        return hash((self.green_level, self.red_level, self.blue_level))

    def __mul__(self, c):
        """
        Уменьшение контраста умножением на с = [0, 1] экземпляра класса Color
        """
        if c > 1 or c < 0:
            raise ValueError
        else:
            contrast_level = - 256 * (1 - c)
            F = 259 * (contrast_level + 255) / (255 * (259 - contrast_level))
            L_red_new = int(F * (self.red_level - 128) + 128)
            L_green_new = int(F * (self.green_level - 128) + 128)
            L_blue_new = int(F * (self.blue_level - 128) + 128)
            new_color = Color(L_red_new, L_green_new, L_blue_new)
            return new_color

    def __rmul__(self, c):
        """
        Уменьшение контраста умножением на с = [0, 1] экземпляра класса Color
        """
        return self.__mul__(c)


def print_a(color: ComputerColor):
    """
    Дана функция, которая выводит букву А в определенном цвете
    """
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] *
        3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] *
        7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] *
        9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
    #
    red_level = 100
    green_level = 149
    blue_level = 237
    mycolor = Color(red_level, green_level, blue_level)
    print(mycolor)
    #
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))
    #
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)
    #
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(color_list)
    print(set(color_list))
    #
    print(0.5 * red)
    #
    print_a(red)

#!/usr/bin/python3

"""
class Square - A class that defines a square
"""


class Square:
    """Class representing a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Class constructor"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size"""
        return (self.__size)

    @property
    def position(self):
        """Getter for position"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
                # __position[1] represents the row
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
                # __position[0] represents the column 

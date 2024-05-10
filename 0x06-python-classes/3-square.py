#!/usr/bin/python3
"""Square module"""


class Square:
    """Private instance attribute"""
    def __init__(self, size=0) -> None:
        self.__size = size
        """if else statment"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """area function with parameter(self)"""
    def area(self):
        """return area value"""
        return self.__size ** 2

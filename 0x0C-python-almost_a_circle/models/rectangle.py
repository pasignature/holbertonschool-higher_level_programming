#!/usr/bin/python3
"""class Rectangle inherits from Base"""

from models.base import Base

class Rectangle(Base):
    ''''Private instance attributes, 
	each with its own public getter and setter'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation of Private instance attributes'''
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """set property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        '''set height attribute'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates Attributes"""
        atribs = ['id', 'width', 'height', 'x', 'y']
        if args and 0 < len(args) <= 5:
            for i, arg in enumerate(args):
                if i == 0:
                    super().__init__(arg)
                else:
                    self.__setatribs__(atribs[i], arg)
        elif kwargs and 0 < len(kwargs) <= 5:
            for c, d in kwargs.items():
                if c == 'id':
                    super().__init__(d)
                elif c in atribs:
                    self.__setatribs__(c, d)

    def area(self):
        '''Method returns area of class Rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Method for printing  Rectangle to stdout'''
        print('\n' * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        '''Method returns string rep. of rectangle '''
        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    @property
    def x(self):
        """set property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        '''set x positional attribute'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """set property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        '''set y positional attribute'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def to_dictionary(self):
        '''Method returns dictionary rep of rectangle'''
        to_dict = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return to_dict

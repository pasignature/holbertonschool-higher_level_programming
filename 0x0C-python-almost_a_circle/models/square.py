#!/usr/bin/python3
'''Square module'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class inherit from rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor Instantiation'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print attribute using __str__'''
        a, b, c, d = self.id, self.x, self.y, self.size
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    @property
    def size(self):
        """set width"""
        return self.height

    def to_dictionary(self):
        '''return dictionary rep of square'''
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic

    @size.setter
    def size(self, value):
        '''set size'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.height = value

    def update(self, *args, **kwargs):
        '''args for rectangle'''
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

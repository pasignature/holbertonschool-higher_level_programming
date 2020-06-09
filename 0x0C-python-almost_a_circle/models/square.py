#!/usr/bin/python3
'''Square Class Module'''
from models.rectangle import Rectangle

class Square(Rectangle):
    '''Square class '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiation of Square attriutes'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set the width"""
        return self.width

    @size.setter
    def size(self, value):
        '''set size'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        '''Set up args for rectangle'''
        atribs = ['id', 'size', 'x', 'y']
        if args and 0 < len(args) <= 4:
            for arg_index, arg in enumerate(args):
                if arg_index == 0:
                    super().updateatribs(arg)
                else:
                    self.__setatribs__(atribs[arg_index], arg)
        elif kwargs and 0 < len(kwargs) <= 4:
            for l, m in kwargs.items():
                if l == 'id':
                    super().updateatribs(id=m)
                elif l in atribs:
                    self.__setatribs__(l, m)

    def __str__(self):
        '''print attribute with __str__'''
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return dictionary repr"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

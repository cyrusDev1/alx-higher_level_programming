#!/usr/bin/python3
"""Defines Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print description of square"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Get or Set size of square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """Update attributs"""
        if args and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    super().__init__(self.size, self.size, self.x, self.y, v)
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    super().__init__(self.size, self.size, self.x, self.y, v)
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

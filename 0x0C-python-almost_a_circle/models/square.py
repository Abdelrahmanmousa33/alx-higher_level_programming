#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return print  representation of a Square."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x,
                        self.y, self.width))

    @property
    def size(self):
        """Get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigins new argument to each attribute"""
        lenth = len(args)
        if lenth and args != 0:
            if lenth >= 1:
                self.id = args[0]
            if lenth >= 2:
                self.size = args[1]
            if lenth >= 3:
                self.x = args[2]
            if lenth >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v


if __name__ == "__main__":
    unittest.main()

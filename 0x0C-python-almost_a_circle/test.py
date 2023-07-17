    def update(self, *args, **kwargs):
        """Assigins new argument to each attribute"""
        lenth = len(args)
        if lenth and args != 0:
            if lenth >= 1:
                self.id = args[0]
            if lenth >= 2:
                self.width = args[1]
            if lenth >= 3:
                self.height = args[2]
            if lenth >= 4:
                self.x = args[3]
            if lenth >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v






    def area(self):
        """ Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the Rectnagle using """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the st nd prin repersention of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x,
                        self.y, self.width,
                        self.height))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return self.__dict__

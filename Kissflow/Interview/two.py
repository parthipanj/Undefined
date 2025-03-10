class A:
    def __init__(self):
        self.x = 1
        self._y = 2
        self.__z = 3

    def get_y(self):
        return self._y


class B:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30

    def get_y(self):
        return self.y


class C(A, B):

    def __init__(self):
        super().__init__()

    def get_x(self):
        return self.x

    def get_y(self):
        return super().get_y()

    def get_z(self):
        return self.z


if __name__ == "__main__":
    c = C()
    print(c.get_x())
    print(c.get_y())
    print(c.get_z())

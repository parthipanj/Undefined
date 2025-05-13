class A:

    def __init__(self):
        print("init a")

    def get_field(self):
        print("A")


class B(A):

    def __init__(self):
        super().__init__()

        print("init b")

        self.temp = "sk"

    def get_field(self):
        print("B")


class C(B):

    def __init__(self):
        super().__init__()

        print("c")

    def diffmethod(self):
        print(self.temp)


obj = C()

obj.diffmethod()

class A:
    def __init__(self):
        print('A init')

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class B(A):

    def __init__(self):
        super().__init__()
        print('B init2')

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print('feature 4 is working')


class C:
    def __init__(self):
        print('C init')

    def feature4(self):
        print('feature 4 is working')

    def feature5(self):
        print('feature 5 is working')


class D(C, A):  # method resolution order MRO is work in left most order
    def __init__(self):
        super().__init__()
        print('hello')


b1=D()

class A:
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class B(A):
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print('feature 4 is working')


class C(B):  # grandchild call
    pass


class D:
    def hello(self):
        print('hello')


class E(A, D):  # call many classes in one class
    pass


"""
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1 = C()
c1.feature1()
e1 = E()
e1.hello()
e1.feature1()
e1.feature2()  """

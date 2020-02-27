class Car:
    wheels = 4
    def __init__(self):
        self.mil=10
        self.name = 'BMW'


c1=Car()
c1.wheels=6
print(c1.name, c1.mil, c1.wheels)
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop('dell','i7')

    def show(self):
        print(self.name, self.roll)
        self.lap.ShowLap()

    class Laptop:
        def __init__(self, brand, con):
            self.brand=brand
            self.con = con


        def ShowLap(self):
            print('brand is', self.brand , self.con)


student = Student('saimun','100')
student2 = Student('kala','200')
student.show()
#student.lap.ShowLap()

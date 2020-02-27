""" class method, Instance Methods, Static Methods """


class Student:
    schoolName = 'Daffodil International University'

    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # Instance Methods

    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    @classmethod
    def schoolNamee(cls):
        return cls.schoolName

    @staticmethod
    def info():
        print('Hello Student of DIU')

    @staticmethod
    def hello():
        print('hello')


st1 = Student(10, 20, 30)
st2 = Student(30, 80, 62)
print(st2.avg())
print(Student.schoolNamee())
Student.info()
Student.hello()
st1.info()
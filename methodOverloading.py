class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        res=0

        if a!= None and b!= None and c!= None:
            res = a + b + c
            return res

        elif a!= None and b!= None:
            res = a + b
            return res
        else:
            res=a
            return res


S=Student(10,30)
print(S.sum(50,50))
print(S.sum(50,50,200))
print(S.sum(50))
print(S.sum())
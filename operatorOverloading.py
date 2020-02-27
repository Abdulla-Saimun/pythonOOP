# same name but parameter is different is called overloading
# in student class avg(a,b) and avg(a,b,c) is called overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3 =Student(m1,m2)
        return s3

    def __gt__(self, other):
        m1= self.m1+self.m1
        m2=other.m1+other.m2
        if(m1>m2):
            return True
        else:
            return False
    def __mul__(self, other):
        v1=self.m1+self.m2
        v2=other.m1+other.m2
        v3= Student(v1,v2)
        return v3

s1 = Student(20, 30)
s2 = Student(60, 70)
s3 = s1+s2
s4=s1*s2
print(s4)

print(s3.m2)

if s1>s2:
    print('S1 wins')
else:
    print('S2 wins')

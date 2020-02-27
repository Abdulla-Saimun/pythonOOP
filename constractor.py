class Computer:
    globalVariable = 30

    def __init__(self,like):
        self.name = 'salman'
        self.age = 30
        self.like=like
    def config(self):
        print(self.name, self.age, self.like)
    print(globalVariable)
c1 = Computer('red')
c1.config()


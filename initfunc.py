class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is: ", self.cpu, self.ram)

inp1=input("Enter the Cpu: ")
inp2=input("Enter ram: ")

com1 = Computer(inp1, inp2)
#com2 = Computer('i6', '8gb')
com1.config()
#com2.config()

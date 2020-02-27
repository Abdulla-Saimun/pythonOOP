class Phycharm:
    def execute(self):
        print('running')
        print('compiling')


class MyEditor:
    def execute(self):
        print('salman')
        print('khan')
        print('running')
        print('compiling')


class Laptop:    # duck typing mean same same do many times without dynamic way. It is not appropriate..

    def code(self, ide):
        ide.execute()

"""a1=MyEditor()
l1=Laptop()
l1.code(a1) """




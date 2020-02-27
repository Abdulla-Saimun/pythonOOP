import urllib.request, urllib.parse, urllib.error

class father:
    def property(self):
        print(' land, house')
    def vehicle(self):
        print('honda car')


class child(father):
    def house(self):
        print('duplex house')


class Anch(child):
    pass


class om:
    def nothing(self):
        print('nothing')


class gan(Anch, om):
    pass


f=father()
c=child()
c.property()
c.vehicle()
a=Anch()
a.house()
g=gan()
print(dir(g))
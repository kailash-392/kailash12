class Avengers:
    def __init__(self, name):
        self.name = name

    def suits(self,powers):
        print("%s --> %s" % (self.name, powers))


class Ironman(Avengers):
    def fetch(self, suit):
        print("%s uses %s" % (self.name, suit))

class CaptainAmerica(Avengers):
    def swatstring(self):
        print("%s uses Sheild" % self.name)



d = Ironman("Tony Stark")
e = CaptainAmerica("Steve Rogers")
print()
print()
d.fetch("Mark 85")
d.suits("Iam IRON-MAN")
print()
print('----------')
print()
e.suits("I can do this all day")
e.swatstring()
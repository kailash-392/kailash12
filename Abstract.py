from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    def noofsides(self):
        print("Don't")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("SEE IN MY ")


class Hexagon(Polygon):

    def noofsides(self):
        print("Laptop")


class Quadrilateral(Polygon):

    def noofsides(self):
        print(".........\***\.........")

R = Triangle()
R.noofsides()


R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

K = Quadrilateral()
K.noofsides()

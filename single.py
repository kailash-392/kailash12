
class Parent:
    def func1(self):
        print("Super7")

class Child(Parent):
    def func2(self):
        print("Agur thu satuho")
object = Child()
object.func1()
object.func2()
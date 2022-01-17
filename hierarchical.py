class Parent:
    def func1(self):
        print("SON OF KING")

class Child1(Parent):
    def func2(self):
        print("KAILASH EMPAIR")

class Child2(Parent):
    def func3(self):
        print("VAMSI EMPAIR")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
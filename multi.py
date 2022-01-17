class a:
    a = ""

    def a(self):
        print(self.a)
class b:
    b = ""

    def b(self):
        print(self.b)
class c(a,b):
    def parents(self):
        print("Father :", self.b)
        print("Mother :", self.a)
s1 = c()
s1.b = "RAJU"
s1.a = "SUJATHA"
s1.parents()
class Myclass(object):
    def set_val(self,val):
        self.val=val

    def get_val(self):
            print(self.val)
a = Myclass()
b= Myclass()
c= Myclass()
d= Myclass()

a.set_val("Kailash")
b.set_val(9.25)
c.set_val("MARVEL KING")
d.set_val("DC QUEEN")


a.get_val()
b.get_val()
c.get_val()
d.get_val()
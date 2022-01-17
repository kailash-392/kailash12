class Person:

    NAME = "Nameless bard"
    def __init__(self,aName):
        self.name =aName
def main():
    aPerson = Person("Finder Myvernspur")
    print(aPerson.name)
main()


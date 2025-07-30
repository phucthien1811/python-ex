class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
        
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Atribute name = " + super().name)
        super().getName()

Bar().getName()
# Ket qua:
# Atribute name = Foo
# Class: Foo
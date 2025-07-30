class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Class: Bar")

print(Foo().name)
Foo().getName()
print(Bar().name)
Bar().getName()

# Ket qua:
# Foo
# Class: Foo
#
# Bar
# Class: Bar
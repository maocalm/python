class Person:
    def setName (self , name ) :
        self.name = name
    def getName(self ):
        return self.name

def fun():
        print("hhhhhhhhhhh")
foo = Person()
foo.setName("han")

print(foo.getName())

foo.setName = fun()
print(foo.getName())
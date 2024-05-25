
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal): # The Dog class inherits all methods of Mammal class.
    def bark(self):
        print("the dog barks!")


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()
print()
cat1 = Cat()
cat1.walk()
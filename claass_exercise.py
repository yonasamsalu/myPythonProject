'''
define a new type(an object) called person these 'Person' objects have a 'name' attribute as well as
  a 'talk' method.
'''
class Person:
    def __init__(self,age):    # this is a constructor function/method.
        self.age = age
    def product(self, x, y):      # it is also a method( a function in a class).

        return (f'the product of the two numbers is {x*y}')

    def student(self,name):
        self.name = name
        print(f'Hi i am {name}')
print()

abi=Person("24")
print(f' i am {abi.age}')
print()

abi.product(6,8)
print(abi.product(6, 8))
print()

abi.student("Yons Amsalu")
print()

bob=Person(27)   # we can use also second class here.
print(f'i am Mark and i am {bob.age}')




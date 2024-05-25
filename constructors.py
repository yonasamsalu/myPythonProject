
class className:
    def __init__(self,x,y):
        self.x= x
        self.y =y

    def draw(self):
        print("hi drawer")

    def move(self):
        print("i want to move")

point=className(12, 16)
print(point.x)
print()


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eating')

class Student(Human):
    pass

    # def __init__(self, name, age, id):
    #     self.name = name
    #     self.age = age
    #     self.id = id
    #     self.nationality = 'Ethiopian'


x = Student('Yonas', 27)

print(x.name)


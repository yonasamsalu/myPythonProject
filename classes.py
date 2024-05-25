class point:
    def draw(self):
        print("hi drawer")
        return 2*3
    def move(self):
        print("i want to move")

a=point()
a.draw()
print()
a.move()
print()
a.x = 23
a.y = 12
print(a.x)
print()
print(a.y)
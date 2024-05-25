def sum(x,y):
    print("hi everybody!")
    return x+y

a=sum(3,8)
print(f'The sum of 3 and 8 is: {a}')
print()

def square_and_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube

result1, result2 = square_and_cube(3)
print(result1)  # Output will be 9
print()
print(result2)  # Output will be 27

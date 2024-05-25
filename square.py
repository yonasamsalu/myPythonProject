

def square(x):
    y=[]
    for i in x:
        t = i**2
        y.append(t)
    return y

x = [1, 2,3]
a = square(x)

print(a)
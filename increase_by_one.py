

def increament(numbers):
    a = []
    for item in numbers:
        item += 1
        a.append(item)
    return a
s = increament([8,3,15])
print(s)
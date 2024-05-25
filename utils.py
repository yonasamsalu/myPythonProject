print()
def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
    return f'The largest number is {maximum}'


numbers = [6, 2, 7, 43, 15]
a = find_max(numbers)
print(a)



numbers= [5, 6, 23, 32, 4, 62, 9, 16, ]
largest= numbers[0]
for x in numbers:
    if x > largest:
        largest=x
print(f'The largest  number is: {largest}')
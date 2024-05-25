for x in range(3):
    for y in range(2):
        print(f' ({x}, {y})' )
print()

y= [5, 2, 5, 2, 2]
for z in y:
    out_put= ""
    for count in range(z):
        out_put += 'x'
    print(out_put)
print()

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()
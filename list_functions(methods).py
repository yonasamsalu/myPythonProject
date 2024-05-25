#  we can use triple quotes(""") to create a multiline string.
numbers=[2,4,3,6,5,9,8]

numbers.append(23) # add a number at the end of the list.
print(f' 23 will be inserted at the end then the list will be:  {numbers}')
print()  # to get in a new line.

numbers.insert(3,43) # to insert 43 at index 3( i.e fourth index).
print(f'we insert 43 at index 3 then the list will be: {numbers}')
print()

numbers.remove(6)
print(f"6 will be removed then the list be: {numbers} ")
print()

print(f'The position of of 9 is in index : {numbers.index(9)}') # it tells us the positin of number 9.
print()

numbers.pop()   #to remove the last item on the list.
print(numbers)
print()


print( 4 in numbers)  # check the existance of an item and returns a boolean value.
print()

print(numbers.count(8))  # count occurances of an item.
print()

numbers.sort()   # sort lists in ascending order.
print(numbers)
print()

numbers.reverse()
print(numbers)
print()

numbers=[2,4,3,6,5,9,8]
numbers2=numbers.copy() # copy of the original list and is not impacted by ather operations.
numbers.append(32)
print(numbers2)



#print(f' the lists are removed!  {numbers.clear()}')  # remove all items and return None.








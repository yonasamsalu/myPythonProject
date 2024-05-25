#EXERCISE: write a program to remove the duplicates in the list.

numbers= [4,6,2,2,4,7,9]
uniques=[]

for item in numbers:
     if item not in uniques:
         uniques.append(item)
print(uniques)  # remove the duplicated item.
print()


original_list = [4,7,8,9,23,7,3,9,4]
unique_list = list(set(original_list))
print(unique_list)   # remove the duplicated item and put in ascending order.
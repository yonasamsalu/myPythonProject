print()
'''
 4. Write a program to remove characters from a string starting from zero 
up to n and return a new string.
'''
def remove_char(word , n):
    x = word[n:]
    return x

x = remove_char("pynative", 4)
#print(f'a new string is: {x}')




'''
  5. Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.
'''
def check_list(numbers):
    for item in numbers:
        if numbers[0] == numbers[-1]:    # numbers[-1] is the last element of a list in python.
            return True
        elif numbers[0] != numbers[-1]:
            return False

x = check_list([4,5,2,3,8,1,7,4])
#print("the result is ", x)




'''
  6. Iterate the given list of numbers and print only 
  those numbers which are divisible by 5
'''

def divisible(lists):
    new_list = []
    for item in lists:
        if item % 5 == 0:
         new_list.append(item)
    return new_list       
            
lists = [10, 20, 33, 46, 55]  
output = divisible(lists)
#print(output)




'''
  7. Print the following pattern
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5   
'''
def number_pattern():
     for i in range(6):
         for j in range(i):
             print(i, end = "" )
         print()

#number_pattern()




'''
  8. Write a program to check if the given number is a palindrome number.

    A palindrome number is a number that is the same after reverse. 
    For example, 545, is the palindrome numbers
'''
def palindrom_number(numbers):
    if numbers[0] == numbers[-1]:
        print("yes. the given number is palindrome.")
    else:
        print("no. the given number is not palindrom.")    

#palindrom_number([1,2,1])




def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

# palindrome(121)
# print()
# palindrome(125)


'''
 8. Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new 
list should contain odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
'''

def merged_list(numbers1, numbers2):
    new_list = []
    for item in numbers1:
        if item % 2 != 0:
            new_list.append(item)
    for item in numbers2:
        if item % 2 ==0:
            new_list.append(item)
    return new_list        

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
output = merged_list(list1, list2)
print(output)
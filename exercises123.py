# def sum_produt(x,y):
#     sum = x+y
#     produt = x*y
#     return f'the sum: {sum}' , f'the product: {produt}'
# sumachin, productachin = sum_produt(7,4)
# print(sumachin)
# print(productachin)

def sum_product(num1, num2):
    
    
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result = sum_product(20, 30)
#print("the result is ", result)

result = sum_product(40, 30)
#print("the result is ", resul

'''Write a program to iterate the first 10 numbers, and in each iteration,
   print the sum of the current and previous number.'''

def sum_with_for_loop():
    for i in range(1, 11):
        sum = i + (i-1)
        print("sum:",sum)
             
        
 #sum_with_for_loop()
 
''' Write a program to accept a string from the user and display characters
      that are present at an even index number.'''
      

# string = input("Enter a string  ")
# for item in string:
#     if string.index(item) % 2 == 0:
#         print(item)
        
        
        
# string = input("Enter a string: ")
# for index in range(len(string)):
#     if index % 2 == 0:
#         print(string[index])


str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)
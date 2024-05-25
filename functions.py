def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}!") # These two lines of codes are in side the function.
    print("wellcome abroad")


x=greet_user("Markos", "Amsalu")  # we are calling a function.
print(x) # since we have no return statement we will get "None"
print()
greet_user("Merry","Amsalu")
print()

def function_name(x,y):
       # x and y are parameters i.e they are place holders for receiving information.
    product= x*y
    print(f'The product of x and is y is: {product}')
function_name(6,2)
#  6 and 2 are are arguments and they are the actual pieces of information.


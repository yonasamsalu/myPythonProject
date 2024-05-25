
try:
    age=int(input("Enter age: "))
    income = 2000
    risk=income/age
    print(f'your age is {age}')
except ZeroDivisionError:
    print("age can not be zero!")
except ValueError:
    print("invalid value") # if we give 0 value to age that shows an Error if we dont use except ZeroDivisionError.
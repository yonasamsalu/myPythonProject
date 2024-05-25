import random

for i in range(3):
    print(random.randint(10,20)) # prints random integer value from 10 to 20.
    
print()   
members = ['Markos', 'Meron','Solomon']
leader = random.choice(members)
print(leader)
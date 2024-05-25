list= [ 12,5,9,4,8,6,2,4,12,15,9]

y=[]
for x in list:
     if x not in y:
         y.append(x)
print(y)

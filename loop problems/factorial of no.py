x=int(input("enter a number to get the factorial"))
y=1
for i in range(1,x+1,1):
    if i==x+1:
        break
    y=y*i
print(y)
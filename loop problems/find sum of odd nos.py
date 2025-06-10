x=int(input("enter the range"))
y=0
for i in range(1,x+1,2):
    if i==x+1:
        break
    y=y+i
print(y)
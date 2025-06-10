x=int(input("enter the number"))
for i in range(1,x+1,1):
    if i%3==0 and i%5==0:
        print(i,end="  ")
    
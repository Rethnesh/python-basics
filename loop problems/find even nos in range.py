x=int(input("enter the range"))
if x<1:
    print("invalid number")
i=1
while i<=x:
    if i%2==0:
        print(i)
    i+=1

def even(x):
    i=0
    while i<=x:
      if i%2==0:
        print(i)
      i+=1
x=int(input("enter the range"))
even(x)
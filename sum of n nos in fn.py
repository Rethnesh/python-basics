def sumofn(x):
           y=0
           i=1
           while i<=x:
              if i==x+1:
                break
              y=y+i
              i+=1
           print(y)
x=int(input("enter the number"))
sumofn(x)
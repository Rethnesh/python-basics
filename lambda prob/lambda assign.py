x=[2,4,67,90,35]
y=list(map(lambda a: a*a,x))
print(y)

x=[21,5,78,35,23,9,8,6]
y=list(filter(lambda a:a%2!=0,x))
z=list(map(lambda b:b*2,y))
print(z)

x=[34,48,87,21,8,9]
y=list(filter(lambda a: a%2==0,x))
print(y)

x=["dry","orange","apple","cherry",'quava',"blueberry","mango","banana"]
y=list(filter(lambda a: len(a)>3,x))
z=list(map(lambda b: len(b),y))
print(z)

x=[23,3,-9,-65,34,2]
y=list(filter(lambda a: a<0,x))
print(y)

x=[3,34,8,21,7,34,9,11]
y=list(filter(lambda a: a%2!=0,x))
z=list(map(lambda b: b*b,y))
print(z)

x=lambda a: a==a[::-1]
y="triirt"
print(x(y))

k=["apple","ant","bat","ball","and"]
l=list(filter( lambda a: a[0]=="a",k))
print(l)
 
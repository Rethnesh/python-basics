x=[3,34,8,21,7,34,9,11]
y=list(filter(lambda a: a%2!=0,x))
z=list(map(lambda b: b*b,y))
print(z)
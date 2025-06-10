x=[21,5,78,35,23,9,8,6]
y=list(filter(lambda a:a%2!=0,x))
z=list(map(lambda b:b*2,y))
print(z)
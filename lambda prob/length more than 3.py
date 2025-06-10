x=["dry","orange","apple","cherry",'quava',"blueberry","mango","banana"]
y=list(filter(lambda a: len(a)>3,x))
z=list(map(lambda b: len(b),y))
print(z)
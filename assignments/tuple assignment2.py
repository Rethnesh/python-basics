x=("cherry","mango","apple","orange","lemon")
print(x)
print(len(x))
print(type(x))
print(x[2])
print(x[1:3])
print(x[:3])
print(x[1:])
print(x[-2])
print(x[-2:-1])
print(x[:-1])
print(x[-3:])
for i in x :
    print(i)
print("lemon" in x)
print("avocado" in x)
print("lemon" not in x)
print("avocado" not in x)
y=list(x)
print(y)
print(type(y))
y.append("watermelon")
y[1]="blueberry"
print(y)
y.pop()
y.pop(1)
print(y)
x=tuple(y)
print(x)
z=("pappaya",)
print(x+z)
p=x+z
print(p)
print(p*5)
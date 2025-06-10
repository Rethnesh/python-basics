x={"pappaya","apple","mango","avocado","cherry"}
for i in x:
    print(i)
print("cherry" in x)
print("lemon" in x)
print("cherry" not in x)
print("lemon" not in x)
z={"dragon fruit","blueberry","raspberry","watermelon"}
y={"pappaya","apple","mango","avocado","cherry","blueberry","lime"}
x.update(y)
print(x)
x.intersection_update(y)
print(x)
z.difference_update(y)
print(z)
z.symmetric_difference_update(y)
print(z)
p=x|y|z
print(p)
l=p&y
print(l)
k=p-z
print(k)
u=y^p
print(u)
print(p)
p.remove("lime")
p.discard("pineapple")
print(p)
p.pop()
print(p)
p.clear()
print(p)
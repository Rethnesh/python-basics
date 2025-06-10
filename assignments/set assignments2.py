x={"cricket","football","hockey","basketball","volleyball","baseball"}
for i in x:
    print(i)
print("cricket" in x)
print("chess" in x)
print("hockey" not in x)
print("carroms" not in x)
z={"volleyball","hockey","baseball","chess"}
y={"chess","carroms","basketball","football","tennis","cricket"}
x.add("polo")
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
p.remove("tennis")
p.discard('cards')
print(p)
p.pop()
print(p)
p.clear()
print(p)
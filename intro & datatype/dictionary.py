x={"name":"rethnesh","age":25,"school":"sesps","clg":"bpc"}
print(x)
print(len(x))
print(type(x))
print(x["age"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
print("age" in x)
print("address" in x)
print("name" not in x)
print("address" not in x)
x["age"]= 24
print(x)
x.update({"name":"reth"})
print(x)
x["house"]="alappatt"
print(x)
x.update({"degree":"bba"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("degree")
print(x)
x.popitem()
print(x)
del x["clg"]
print(x)
x.clear()
print(x)
del x
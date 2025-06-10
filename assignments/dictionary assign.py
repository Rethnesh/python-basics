x={"a":"apple","b":"banana","c":"cherry","d":"dragonfruit"}
print(x)
print(len(x))
print(type(x))
print(x["c"])
print(x.get("b"))
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
y=x.copy()
print(y)
z=dict(x)
print(z)
x["a"]="avocado"
print(x)
x.update({"a":"apple"})
print(x)
x["m"]="mango"
x.update({"f":"fig"})
print(x)
x.pop("c")
x.popitem()
print(x)
del x["a"]
print(x)
x.clear()
print(x)
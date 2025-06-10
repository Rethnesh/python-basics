x={"a":"ant","b":"bats","c":"cat","d":"deer"}
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
x["a"]="anteater"
print(x)
x.update({"a":"ant"})
print(x)
x["m"]="monkey"
x.update({"f":"fox"})
print(x)
x.pop("c")
x.popitem()
print(x)
del x["a"]
print(x)
x.clear()
print(x)
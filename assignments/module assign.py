import math
import datetime
import module

print(module.plus(10,50))

print(module.sub(23,12))

print(module.multi(8,9))

print(module.divi(10,2))

print(min(56,34,2,34,90,12))

print(max(637,356,234,567))

print(abs(-89))

print(pow(6,4))

print(math.pi)
print(math.atan(90))
print(math.log(90))
print(math.sqrt(64))
print(math.factorial(10))
print(math.ceil(7.12))
print(math.floor(5.93))

x=datetime.datetime.now()
print(x)

print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%D"))
print(x.strftime("%j"))

print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%p"))
print(x.strftime("%X"))

y=datetime.datetime(2000,3,23)
print(y.strftime("%A"))

r=int(input("enter the radius"))
print("circumference of circle is")
print(math.pi*r*2)

r=int(input("enter the radius"))
h=int(input("enter the height"))
print("volume of cone")
print(math.pi*r*r*h/3)

r=int(input("enter the radius"))
print("area of sphere is")
print(4*math.pi*r**2)
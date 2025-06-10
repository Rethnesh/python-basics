# def plus(x,y):
#     return x+y
# print(plus(4,2))

# def factorial(x):
#     y=1
#     for i in range(1,x+1,1):
#         if i==x+1:
#             break
#         y=y*i
#     return(y)
# x=int(input("enter the no: to get factorial"))
# print(factorial(x))
        
# def fn(x=7):
#     print(x+10)

# fn()

# def skip():
#     pass

# x=lambda a,b: a+b
# print(x(4,5))

# y=lambda f,g,h: f*g*h
# print(y(2,3,4))

# x=["apple","berry","cherry","dates"]
# y= list(map(lambda a: a.upper(),x))
# print(y)

x=[4,45,8,3,73,24]
y=list(filter(lambda a: a>20, x))

print(y)
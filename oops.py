# class  name:
#     x=10
# obj=name()

# print(obj.x)

# class add:
#     x=10
#     y=5
#     z=x+y

# obje=add()

# print(obje.z)

# class fruit:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#     def  plus(self):
#         z=self.x+self.y
#         print(z)

# taste=fruit(6,7)
# print(taste.x,taste.y)
# taste.plus()

#INHERITENCE

class age:
    def __init__(self,x,y):
        self.student=x
        self.teacher=y
    def difference(self):
        z=self.teacher-self.student
        print(z)
class name(age):
    pass

obj=name(12,45)
obj.difference()

class new:
    pass




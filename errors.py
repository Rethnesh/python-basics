# try:
#     print(X)
# except:
#     print("error found")

# try:
#     print(x)
# except NameError:
#     print("the variable is not defined")
# except:
#     print("error found")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("check the divisor")
# except:
#     print("error")

# x=3

# try:
#     print(x)
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("completed")

y=int(input("enter a number"))
if y<0:
    raise Exception("negative no not allowed")
else:
    print(y)
# print("hi")
# print("Bye")
# #  compile time error
# printt("Hey")

# # logical error
# a=10
# b=20
# print(a+a)

# # runtime error
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# print(a+b)

# try:
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     print(a+b)
# except Exception as e:
#     print("something",e)

# try:
#     a=input("Enter a: ")
#     b=input("Enter b: ")
#     # print(a+b)
#     print(a/b)
# except Exception as e:
#     print("something",e)

# try:
#     a= int(input("Enter :"))
# except ValueError as e:
#     print("Value Error",e)


# try:
#     a= int(input("Enter :"))
#     b=int(input())
#     c=input()
#     print(c/a)
# except ValueError as e:
#     print("Value Error",e)
# except TypeError as e:
#     print("Type Error",e)
# except Excception:
#     print("Something wrong")

# try:
#     a= int(input("Enter :"))
#     b= int(input("Enter :"))
#     c=input()
#     print(d)
# except ValueError as e:
#     print("Value Error",e)
# except TypeError as e:
#     print("Type Error",e)
# except Exception:
#     print("Something wrong")


try:
    a= int(input("Enter :"))
    b= int(input("Enter :"))
except ValueError as e:
    print("Value Error",e)
except TypeError as e:
    print("Type Error",e)
finally:
    print("done")
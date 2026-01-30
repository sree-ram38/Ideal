# def data():
#     print("My name is sreeram")
# data()

# def data():
#     return "my name is sreeram"
# print(data())

# s_username = "Emc"
# s_password = 123
# uname = input("Enter your name : ")
# password = int(input("Enter the password : "))

# def validate():
#     if(s_username==uname and s_password==password):
#         print("True")
#     else:
#         print("False")
# validate()


# s_username = "Emc"
# s_password = 123
# uname = input("Enter your name : ")
# password = int(input("Enter the password : "))

# def validate():
#     if(s_username==uname and s_password==password):
#         return True
#     else:
#         return False
# print(validate())


a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
def add(a,b):
    sum = a+b
    return sum

added = add(a,b)
final = added * c
print("The final answer : ",final)
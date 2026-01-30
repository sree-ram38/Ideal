# age = int(input("Enter your age: "))

# if age>=18:
#     print("You are eligible to vote")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are not eligible to vote")



# request = input("Do you need to go out(Y/N): ")
# if request == "Y":
#     print("You are allowed to go out")
# else:
#     print("You are not allowed to go out")


operator = input("Enter the operator (+ - * /) : ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print(f"{operator} is a invalid operator") 0
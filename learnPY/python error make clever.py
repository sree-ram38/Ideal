# a=10
# b=20
# print(type(a))
# print(a+b)

# a="10"
# b="20"
# c=a+b
# print(c)

# # type casting
# a=int("10")
# b=int("20")
# c=a+b
# print(c)


# a=int(input("Enter the value of a : "))
# b=int(input("Enter the value of b : "))
# c=a+b
# print(c) 

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# address = input("Enter your address")
# print(f"My name is {name}")
# # or print("My name is",name)
# print(f"My age is : {age}")
# print("My address is ",address)

# a=int(input("Enter the value of a : "))
# b=int(input("Enter the value of b : "))
# c=int(input("Enter the value of c : "))
# mul=a*b*c
# add=a+b+c
# divide=mul/add
# print("The divided valuee is ",divide)

# name = input("Enter your name : ")
# score = int(input("Enter your score : "))
# department = input("Enter your department : ")
# print(f"My name is {name}")
# print(f"My score is ",score/10)
# print(f"My department is ",department)


# print("min"=="min")
# csk="win"
# csk="lose"
# if(csk=="win"):
#     print("The cup is ours")
# else:
#     print("As regular the cup is not ours")


# meghna=input("Enter : ")
# if(meghna=="died"):
#     print("Surya meets priya")
# else:
#     print("Surya weds meghna")

# mark=int(input("Enter your mark : "))
# if (mark > 35):
#     print("Pass")
# else:
#     print("Fail")

# income = int(input("Enter your income : "))
# if (income >= 7000):
#     print("Eligible for scholarship")
# else:
#     print("Not eligible for scholarship")

# number=int(input("Enter the number : "))
# if(number%5==0 and number%3==0):
#     print("The number is divisible by 3 and 5")
# else:
#     print("The number is not divisible by 3 and 5")

# number=int(input("Enter the number : "))
# if(number%2==0):
#     print("It is even")
# else:
#     print("It is odd")


# score=int(input("Enter your score : "))
# if(score<35):
#     print("Poor student")
# elif(score>=35 and score<=70):
#     print("Average student")
# elif(score>70 and score<=100):
#     print("Good student")
# else:
#     print("Invalid score")

# #mini calculator
# a=int(input("Enter the value of a : "))
# b=int(input("Enter the value of b : "))
# operation=input("Enter the operation to be done : ")
# if (operation=="add"):
#     add=a+b;
#     print(f"The added value is {add}")
# elif(operation=="sub"):
#     sub=a-b;
#     print(f"The subracted value is {sub}")
# elif(operation=="mul"):
#     mul=a*b;
#     print(f"The multiplied value is {mul}")
# elif:
#     div=a/b
#     print(f"The divided value is {div}")
# else:
#     print("Invalid operation")


# score = int(input("Enter the value : "))
# if(score>=70):
#     input("Enter your name : ")
#     input("Enter your department : ")
#     input("Enter your location : ")
#     print("You are eligible")
# else:
#     print("You are not eligible")


# salary=int(input("Enter your salary : "))
# age= int(input("Enter your age : "))
# if(salary>=20000 or age<=25):
#     loan=int(input("Enter the required loan amount : "))
#     if(loan<=50000):
#         print("You are eligible for loan")
#     else:
#         print("Maximum loan amount is 50000")
# else:            
#     print("You are not eligible")

# sub1 = int(input("Enter the mark of sub 1 : "))
# sub2 = int(input("Enter the mark of sub 2 : "))
# sub3 = int(input("Enter the mark of sub 3 : "))
# sub4 = int(input("Enter the mark of sub 4 : "))
# sub5 = int(input("Enter the mark of sub 5 : "))
# add=sub1+sub2+sub3+sub4+sub5;
# avg=add/5;
# if(avg<35):
#     print("Additional class is required")
# else:
#     print("You are good to go")


# # for loop
# for i in "Apple":
#     print(i)

# for i in range(1, 10):
#     print(i)

# for i in range(11, 21):
#     print(i ," x  2 = ",i*2)

# limit=int(input("Enter the limit : "))
# add = 0
# for i in range(1,limit+1):
#     num=int(input(f"Enter the value {i} : "))
#     add+=num
# print(f"Sum is {add}")  

# num1 = int(input("Enter the value : "))
# num2 = int(input("Enter the value : "))
# for i in range(num1 , num2+1):
#     print(i)


# num1 = int(input("Enter the value : "))
# num2 = int(input("Enter the value : "))
# for i in range(num1+1 , num2):
#     print(i)

# limit = int(input("Enter the limit : "))
# for i in range(1,limit+1):
#     if (i%2== 0):
#         print(i)


# limit = int(input("Enter the limit : "))
# add = 0
# for i in range(1,limit+1):
#     if (i%2== 0):
#         add+=i
# print(add)


# limit = int(input("Enter the limit : "))
# add = 0
# for i in range(1,limit+1):
#     if (i%2== 0):
#         add+=1
# print(add)


# limit = int(input("Enter the limit : "))
# even = 0
# odd = 0
# for i in range(1,limit+1):
#     if (i%2== 0):
#         even+=1
#     else:
#         odd+=1
# print("Count of odd : ",odd)
# print("Count of even : ",even)


# count=0
# for i in range(1,101):
#     if (i%3==0 and i%5==0):
#         count+=1
# print(count)


# count=0
# for i in range(1,101):
#     if (i%3==0 and i%5==0):
#         count+=1
#         print(i)
# print("The number divisible by 3 and 5 between 1 to 100 is ",count)

# add=0
# for i in range(1,6):
#     add+=i
# print("The sum of first five natural number is ",add)


# # wrong
# user = int(input("Enter the limit : "))
# count = 0
# avg = 0
# for i in range(1,user+1):
#     num = int(input(f"Enter the number {i} : "))
#     count+=num
# print("The count is : ",count)

# a=[]
# for i in range(10):
#     num = int(input("Enter the value to be inserted in list : "))
#     a.append(num)
# print("The values in the list are : ",a)


# a=[]
# for i in range(1,6):
#     num = int(input(f"Enter the value to be inserted in list {i} : "))
#     a.append(num)
# print("The values in the list are : ",a)
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# a=[]
# for i in range(5):
#     num = int(input("Enter the value to be inserted in list "+str(i+1)+" : " ))
#     a.append(num)
# print("The values in the list are : ",a)
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# # cube
# for i in range(1,6):
#     cube=i*i*i
#     print(f"Number is : {i} and the cube of the {i} is : ",cube)



# Nested for loop

# for i in range(1,10):
#     for j in range(1,3):
#         print(i,"Berry")


# for i in range(1,4):
#     print(f"week : {i}")
#     print("............................")
#     for j in range(1,4):
#         print(f"Day : {j}")


# for i in range(1,5):
#     print("*", end="")

# for i in range(1,5):
#     print()
#     for j in range(1,i+1):
#         print(j,end="")

# for i in range(1,5):
#     print()
#     for j in range(1,i+1):
#         print("*",end="")


# while loop


# i=0 or i=1
# while i<=5:
#     print("*" *i)
#     i+=1

# i=0
# while(i==0):
#     print(i)
#     i=1;
#     # break;

# i=1
# while(i<=5):
#     print(i)
#     i=i+1
#     # print(i)

# i=-200
# while(i<=200):
#     print(i)
#     i=i+10
#     # print(i)

# printing the value in reverse order
# i=10
# while(i>0):
#     print(i)
#     i-=1
    
# factorial
i=3
fact=1
while(i>0):
    fact*=i
    i=i-1
print(fact)
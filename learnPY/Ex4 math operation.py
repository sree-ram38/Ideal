# mathoperation
# number = 5

# number = number+1
# number+=1
# number = number-1
# number = number*1
# number = number/1
# number = number**2
# number = number%2
# print(number)




# math function
# a = 4.17
# b = 7
# c = 9

# roundingoff = round(a)
# absolute = abs(b)
# power = pow(5, 3)
# minimum = min(a,b,c)
# maximum = max(a,b,c)
# print(roundingoff)
# print(absolute)
# print(power)
# print(minimum)
# print(maximum)      


import math
# print(math.pi)
# print(math.e)
# print(math.pi*21)
# print(f"The value of pi is {math.pi} and the value of e is {math.e}")

# a = 20
# print(math.sqrt(a))
# #ceil will round the value up
# b = 20.2
# print(math.ceil(b))
# #floor will round the value down
# c = 20.6
# print(math.floor(c))


# # Radius of the circle
# r = int(input("Enter the radius = "))
# pi = math.pi
# value = 2*pi*r
# print(f"The radius of the circle is {value}")
# print(f"The radius of the circle is {2*pi*r}")
# print(f"The radius of the circle is",{value})  


## Area of the circle
# radius = float(input("Enter the radius of the circle ="))
# pi = math.pi
# value = pi*pow(radius,2)
# print(f"The radius of the circle is {pi*radius*radius}")
# print(f"The radius of the circle is {round(value)}")


##Hypothesis of the triangle
a = int(input("Enter the value of a ="))
b = int(input("Enter the value of b ="))

powerA = math.pow(a,2)
powerB = math.pow(b,2)
value = powerA + powerB
print(f"The Hypothesis of a triangle is {math.sqrt(value)}")
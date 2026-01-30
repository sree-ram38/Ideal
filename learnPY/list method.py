num = [3, 4, 5, 8, 1]

# #add to the last of the list
# num.append(12)

# # add to beggining of the list
# num.insert(0, 10)

# #remove the value from list
# num.remove(4)

## clear all the value in the list
# num.clear()

# #remove last item in the list
# num.pop()

# # return the index of the value in the list
# a=num.index(5)
# print(a)

# # return in boolean value
# print(50 in num)

# # count the same value in the list
# print(num.count(5))

# # it will sort the list in ascending order
# num.sort()
# #if we descinding order of the list after sorting use reverse() function
# num.reverse()

# # copy the original list to the another variable we want
# num2 = num.copy()
# num.append(10)
# print(num,num2) 

num1=[2, 2, 3, 3, 5, 6, 3, 4, 7, 8,]
empty=[]
for i in num1:
    if i not in empty:
        empty.append(i)
print(empty)

# # this is for all other operation above
# print(num)

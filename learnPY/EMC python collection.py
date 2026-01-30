# a=[]
# print(type(a))


# append is used to add the value to the last of the existing list
# a=[]
# a.append(10)
# print(a)

# a = [12,34,56,32,41]
# print(a[0])

# To add the value first of the list you need to use insert
# a = [12,34,56,32,41]
# a.insert(0,89)
# print(a)

# to insert the value instead of that
# a = [23, 34, 46]
# a[0]=25
# print(a)

# to remove the value from the list
# a = [23, 34, 46]
# a.pop(0)
# print(a)

# a = [23, 34, 46]
# a.pop()
# print(a)

# extend two list
# a=[12, 34, 41, 36]
# b=[13, 35, 42, 37]
# a.extend(b)
# print(a)

# # Tuple



# a = (1, 2, 3, 4) 

# b = list(a)

# print(type(a))
# print(a)
# print("\n")
# print(type(b))
# print(b)




# # set
# a={1, 2, 3, 4, 1}
# # a.remove(4)
# a.pop()
# print(a)


# dictionary

data = {
    "name":"sreeram",
    "age":23,
    "location":"nagercoil",
    "nationality":"indian",
    "student":["Aswin","Vinu","Effect","Siva"]
}
# print(data)
# print(type(data))
# print(data["name"])

# This will display only the key in the dictionary
# print(data.keys())

# This will display only the value of the key in the dictionary
# print(data.values())

# to change the value in the dictionary
# data["age"]=22
# print(data)

# to update new key and a value
# data["section"]="Viii"
# print(data)

# # to delete some key in the dictionary
# data.pop("age")
# print(data)

# # To delete the complete dictionary
# del data
# print(data)
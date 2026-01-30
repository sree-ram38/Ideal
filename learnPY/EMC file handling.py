# f=open("fruits.txt","w")
# # print(f)
# # print(f.read())

# # to write anything inside the file 
# f.write("Bannana\n")
# f.write("grape\n")
# f.close()


# f=open("fruits.txt","r+")
# print(f.read())

 
f=open("fruits.txt","a")
f.write("Apple\n")
f.write("Orange\n")
f.close()

f=open("fruits.txt","r+")
# print(f.read())
print(f.readline())
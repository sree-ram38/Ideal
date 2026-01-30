# this is used to create a file using the x mode
# file = open("D:\coding-stuff\learnPY\FileHandling.txt","x")

# it is used to read the file that has been opened
# one = open("D:\coding-stuff\learnPY\FileHandling.txt","r")
# two = one.read()
# print(two)



# I am SREERAM
# From kanyakumari
# I am here to learn and create file handling

# # w is for write mode if the given name is not correct it will create a file in write mode , but if the given file exist it will delete all the data in the existing file in the write mode
# one = open("D:\coding-stuff\learnPY\FileHandling.txt","w")
# one.write("I have learned something in the topic file handling")



# this is correct in r+ mode
# one = open("D:\coding-stuff\learnPY\FileHandling.txt","r+")
# print(one.read())
# one.write("I am learning something to read and write in file handling")


# one = open("D:\coding-stuff\learnPY\FileHandling.txt","r+")
# print(one.tell())
# one.write("Hi")
# print(one.tell())
# print(one.read())
# print(one.tell())


# # w+ mode if you specify the correct name it will do some operation over that file otherwise it will create a new file


# one = open("D:\coding-stuff\learnPY\FileHandling.txt","w+")
# one.write("this is w+")
# one.seek(0)

# data = one.read()
# print(data)
# one.close()




# # append is used only for append any thing to the file, that will append to the last 
# one = open("D:\coding-stuff\learnPY\FileHandling.txt","a")
# one.write(" This is sreeram from kanyakumari, currently I am in ideal corporative service for learning")


# this is a+ mode
one = open("D:\coding-stuff\learnPY\FileHandling.txt","a+")
# one.write(" This is sreeram from kanyakumari, currently I am in ideal corporative service for learning")
one.seek(0)
print(one.read())
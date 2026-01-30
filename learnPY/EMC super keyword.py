# class a():
#     def __init__(self):
#         print("A")

#     def display(self):
#         print("You are in class a")

# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("B")

#     def display(self):
#         print("You are in class b")
 
# obj = b()



# class a():
#     def __init__(self):
#         print("A")

#     def display(self):
#         print("You are in class a")

# class b():
#     def __init__(self):
#         super().__init__()
#         print("B")

#     def display(self):
#         print("You are in class b")

# class c(a,b):
#     def __init__(self):
#         super().__init__()
#         print("C")

#     def display(self):
#         print("You are in class c")   


# obj =c()





class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("You are in class b")

class c(b, a):
    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("You are in class c")   


obj =c()
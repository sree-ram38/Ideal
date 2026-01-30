#  a constructorr is a unique function that gets called automatically when an object is created of a class (init)
# class laptop:
#     def __init__(self):
#         # print("demo")
#         self.price=0
#         self.ram=""
#         self.processor=""
#     def display(self):
#         print("Display")

# the main purpose of a constructor is to initialize or assign values to the data members of that class
# object created
# hp=laptop()

# hp.price=50000
# # print(hp.price)
# hp.ram="12GB"
# hp.processor="i7"
# print(hp.price)

class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram :",self.ram)
        print("processor :",self.processor)
    
hp=laptop()
dell=laptop()

hp.ram="16GB"
hp.processor="i5"

dell.ram="8GB"
dell.processor="i7"

hp.display()
dell.display()

class laptop:
    pass
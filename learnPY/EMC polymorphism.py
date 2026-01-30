# def add(a,b,c=0):
#     print(a+b+c)
# add(10,20)
# add(10,20,30)



# class animal():
#     def sound(self):
#         print("Animal makes sound")

# class dog(animal):
#     def sound(self):
#         print("Dog barks")

# class bird():
#     def sound(self):
#         print("Bird's sing")    

# a1=animal()
# a1.sound()
# d1=dog()
# d1.sound()
# b1=bird()
# b1.sound()




# # polymorphism example
# class shape():
#     def area(self):
#         return 0
# class rectangle(shape):
#     def area(self):
#         l=10
#         b=20
#         print(l*b)

# s1=shape()
# print(s1.area())

# r1=rectangle()
# r1.area()




# class person():
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
#         # print(grade)
    
#     def display(self):
#         print(self.name,self.grade)

# # s1=student("A")
# s1=student("Ram","A")
# s1.display()




# # Base class
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# # Derived class
# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# # Create object of Car
# c = Car()
# c.start()



# Base class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# # Derived class
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display_details(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)

# # Create object of Manager
# m = Manager("Sreeram", 75000, "IT")
# m.display_details()

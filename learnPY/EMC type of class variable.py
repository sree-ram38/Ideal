# type of class variable instance variable and class variable
# class phone:
#     def __init__(self,brand,price,chargertype):
#         self.brand = brand
#         self.price = price
#         self.chargertype = chargertype
#     def display(self):
#         print("Brand :",self.brand)
#         print("PRice :",self.price)
#         print("ChargerType :",self.chargertype)

# samsung = phone("Samsung","10000","B-Type")
# samsung.display()print("\n")

# vivo = phone("vivo","20000","B-Type")
# vivo.display()

# google = phone("google","20000","B-Type")
# google.display()



# creating a variable
class phone:
    chargertype = "C-Type"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand :",self.brand)
        print("PRice :",self.price)
        print("ChargerType :",self.chargertype)

samsung = phone("Samsung","10000")
samsung.display()
print("\n")

vivo = phone("vivo","20000")
vivo.display()
print("\n")

google = phone("google","20000")
google.display()

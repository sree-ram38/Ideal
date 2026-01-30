# single inheritance
# class dad:
#     def phone(self):
#         print("Dads phone")

# class son(dad):
#     def laptop(self):
#         print("Sons laptop")

# ram = son()
# ram.phone()


# multiple inheritance more than two class can be accessed by one class
# class dad():
#     def phone(self):
#         print("Dads phone")

# class mom():
#     def sweet(self):
#         print("Mom's sweet")

# class son(dad, mom):
#     def laptop(self):
#         print("Sons laptop")

# ram=son()
# ram.phone()
# ram.sweet()




# # multi level inheritance()
# class grandpa():
#     def phone(self):
#         print("Grandpa's phone")

# class dad(grandpa):
#     def money(self):
#         print("dad's phone")

# class son(dad):
#     def laptop(self):
#         print("son's phone")

# ram = son()
# ram.laptop()
# ram.money()
# ram.phone()

# d1 = dad()
# d1.phone()

# # Hierarchical inheritance if one class is inherit by more than two class then it is a hierarchical
# class dad():
#     def money(self):
#         print("dad's money")

# class son1(dad):
#     pass

# class son2(dad):
#     pass

# class son3(dad):
#     pass

# ram = son1()
# ram.money()




# hybrid inheritance
class dad():
    def money(self):
        print("dad's money")

class land():
    def important(self):
        print("Important land")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

ram = son1()
ram.land()
ram.money()
# creating a class
class goa:
    name=""
    drink=""
    def party(self):
        print("let's party")     
    def beach(self):
        print("Enjoying the beach")

velu = goa()
shawn = goa()

velu.name = "velayutham"
shawn.name = "shawn shaffin"

velu.drink = "no"
shawn.drink = "yes"

print(velu.name)
print("drink : ",velu.drink)
print(shawn.name)
print("drink : ",shawn.drink)

velu.beach()
shawn.party()














# using the object created we can access the function inside the class
# velu.beach()
# shawn.party()

# we can use the object to access the variable inside the class
# print(velu.drink)

# to set the value for the variable
# setvalue = velu.drink ="Hot Water"
# print(velu.drink)

# setvalue = shawn.drink = "Chill water"
# print(shawn.drink)

# velu.name = "velayutham"
# print(velu.name)

# #object name.variable name inside the class = value to be added 
# shawn.name = "Shawn shaffin"

# print(shawn.name)
# # print(object name.variable name inside the class)
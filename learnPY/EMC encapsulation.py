class company():
    def __init__(self):
        self.__companyname="google"
    def companyname(self):
        print(self.__companyname)

c1=company()
c1.companyname()
print(c1.__companyname)
# no underscore - public, one underscore - protected, two underscore - private
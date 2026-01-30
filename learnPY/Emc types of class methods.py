class laptop:
    chargertype = "c-type"

    def __init__(self):
        self.brand=""
        self.price=45
    
    def setprice(self,price):
        self.price=price
    
    def getprice(self):
        print(self.price)

    # classmethod
    def changechargertype(cls):
        cls.chargertype="B-Type"
        print("Charger type changed to B")

    # staticmethod    
    def info():
        print("This is laptop class")

hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()
hp.info()
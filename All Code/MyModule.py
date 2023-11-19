# name ="Raunak"
# price = 0
class MyModule:
    def ModuleInfo(self):
        print("Module Version: 12.2")
        print("This is custom module")
        print("This Module made by Raunak Gupta\n\n")

    def ModuleOptions(self):
        print("1.Price Set()")
        print("2.Price Show()")
        print("3.Name Set()")
        print("4.Name Show()\n\n")



    # PriceSet
    def PriceSet(self, price):
        self.price = price



    # PriceShow
    def PriceShow(self):
        print(f"price is {self.price}")


    # NameSet
    def NameSet(self,name):
        self.name = name


    # NameShow
    def NameShow(self):
        print(f"price is {self.name}")
    
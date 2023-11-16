'''
Introduction to 
Object Oriented Programming
'''

print("------------------------------------------------\n")

print("1.Creating Class & object")
class Dog:
    pass


obj = Dog()



print("\n------------------------------------------------\n")

print("2.Creating Constructor __init__")
class Dog:
    attr1 = ""
    # Instance attribute
    def __init__(self, name):
        self.attr1 = name
        print(f"Hello there {self.attr1}")

 

str2 = input(str("Enter Name: "))
Dog(str2)


print("\n------------------------------------------------\n")

print("3.Inheritance in class")


class base:
    def getinfo(self,a,b):
        self.a = a
        self.b = b
    

class derived(base):
    def showinfo(self):
        print(f"Age is {self.a}, Name is {self.b}")




derivedObj = derived()

try:
    name = str(input("Enter name: ")) 
    age = int(input("Enter Age: ")) 

except Exception as e:
    print("Error Occured: ", e)

else:
    derivedObj.getinfo(age,name)
    derivedObj.showinfo()



print("\n------------------------------------------------\n")

print("3.Polymorphism in class")





















print("\n------------------------------------------------")

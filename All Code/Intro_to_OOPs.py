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
    # Instance attribute
    def __init__(self, name):
        self.name= name
        print(f"Hello there {self.name}", ", Name by constructor")

    def __del__(self):
        print(f"Hello there {self.name}", ", Name by destructor")

 

str2 = input(str("Enter Name: "))
objdog = Dog(str2)

del objdog

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
print("3.1.Method Overriding")

class car:
    def sound(self):
        print("Car Sound")

    def start(self):
        print("Car Start")

class car1(car):
    def start(self):
        print("Car Start 1")

class car2(car):
    def start(self):
        print("Car Start 2")


carObj = car()
carObj1 = car1()
carObj2 = car2()

carObj.sound()
carObj.start()

carObj1.sound()
carObj1.start()

carObj2.sound()
carObj2.start()


print("\n3.2.Method OverLoading")
class OverloadedMethods:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the class
obj = OverloadedMethods()

# Test different method calls
result1 = obj.add(1)
result2 = obj.add(1, 2)
result3 = obj.add(1, 2, 3)

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

print("\n------------------------------------------------")

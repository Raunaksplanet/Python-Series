'''
Introduction to 
Module and packages
'''

print("------------------------------------------------\n")

'''
A module is a self-contained Python file that contains 
Python statements and definitions, like a file named MYModule.py, 
which can be considered as a module named MYModule which can be 
imported with the help of import statement.
'''


# Importing custom module named "MyModule"
import MyModule

obj = MyModule.MyModule()

obj.ModuleInfo()
obj.ModuleOptions()
obj.PriceSet(100)
obj.NameSet("Raunak Gupta")
obj.PriceShow()
obj.NameShow()



print("\n------------------------------------------------\n")

'''
To create a package in Python, we need to 
follow these three simple steps:

First, we create a directory and give it a package name,
preferably related to its operation.

Then we put the classes and the required functions in it.

Finally we create an __init__.py file inside the directory, 
to let Python know that the directory is a package.
'''


# Import classes from your brand new package 
from MyPackage import Bmw 
from MyPackage import Audi 
    
# Create an object of Bmw class & call its method 
ModBMW = Bmw.Bmw() 
ModBMW.outModels() 
    
# Create an object of Audi class & call its method 
ModAudi = Audi.Audi() 
ModAudi.outModels() 

print("\n------------------------------------------------")
'''-------------------------------------------------------------'''
## Topic Convered:- Comment, escape sequance, Data Types(Mutable,Immutable)
## Topic Convered:- Input & output method, Input & output method
'''-------------------------------------------------------------'''


'''-------------------------------------------------------------'''
# 1.1 this is Single line comment
'''-------------------------------------------------------------'''




'''-------------------------------------------------------------'''
''' 
1.2
This 
is 
Multi 
line
comment 
'''
'''-------------------------------------------------------------'''




'''-------------------------------------------------------------'''
# 1.3 escape sequance
# print("\'Single Quote\'") 
# print("\"Double Quote\"") 
# print("\nNextLine") 
# print("\tTab Space") 
# print("Hello there\rRonak") 
# print("\\ Slash")
'''-------------------------------------------------------------'''




'''-------------------------------------------------------------'''
# list, set, tuple (Mutable)
# int floatstr tuple bool frozen set (Immutable)
# 1.4 Data Types
# 1.4.1.int
x = 5
print(x)

# 1.4.2.float
y = 3.14
print(y)

# 1.4.3.String
message = 'Hello, Python!'
print(message)

# 1.4.4.bool
bool = True
print(bool)

# 1.4.5.list
list = [1, 2, 3, "four"]
print(list)
print(list[2])

# 1.4.6.tuple
tuple = (1, 2, 3)
print(tuple)
print(tuple[1])

# 1.4.7.set
set = {1, 2, 3,3}
print(set)
frzset = frozenset([1,33,4,55,6,3,3])
print(33 in frzset)

# 1.4.8.dict
dict = {"name": "John", "age": 25}
print(dict)
print(dict["name"])

# 1.4.9.Void
no_value = None
print(no_value)
'''-------------------------------------------------------------'''




'''-------------------------------------------------------------'''
# 1.5 Input & output method
name = input("Enter Name: ") 
age = int(input("Enter Age: ")) 

# Concatenate
print("Name:", name, "Age:", age)

# Fstring
print(f"Name: {name} Age: {age}")

# Formated output 1
print("Name: %s Age: %d" %(name,age))

# Formated output 2
print("Name: {} Age: {}" .format(name,age))
'''-------------------------------------------------------------'''




'''-------------------------------------------------------------'''
# 1.6 Conversion Method
print("\nString strr to number")
strr = "24"
num = int(strr)
filoat = float(strr)

print(strr,type(strr))
print(num,type(num))
print(filoat ,type(filoat))

print("\nNumber to string")
filoat = 45.2345
num = 55
strr = str(num)
strr2 = str(filoat)

print(num,type(num))
print(filoat,type(filoat))
print(strr ,type(strr))
print(strr2 ,type(strr2))
'''-------------------------------------------------------------'''

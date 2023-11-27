'''
Introduction to 
Decorators
'''

print("------------------------------------------------\n")

'''
First Class Objects
In Python, functions are first class objects which means that functions in Python can be
used or passed as arguments.

Properties of first class functions:
1.A function is an instance of the Object type.
2.You can store the function in a variable.
3.You can pass the function as a parameter to another function.
4.You can return the function from a function.
'''

# Example 1: Treating the functions as objects. 

def shout(text): 
    return text.upper() 
 
print(shout('Hello')) 
 
yell = shout 
 
print(yell('Hello')) 

print("\n------------------------------------------------\n")

def greet(name):
    return f"Hello, {name}!"

def welcome(name):
    return f"Welcome, {name}!"

def say_hello(func, name):
    message = func(name)
    print(message)

say_hello(greet, "Alice")
say_hello(welcome, "Bob")

print("\n------------------------------------------------\n")

# Passing the function as an argument 
def shout(text): 
    return text.upper() 
 
def whisper(text): 
    return text.lower() 
 
def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 
 
greet(shout) 
greet(whisper) 

print("\n------------------------------------------------")

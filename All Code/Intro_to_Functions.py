'''
Introduction to Functions in python

def function_name(parameters):
    # code to be executed
    return result

'''


print("------------------------------------------------\n")

print("1. Basic Function with parameters")
def add_numbers(a, b):
    result = a + b
    return result

# Call the function
sum_result = add_numbers(5, 3)
print("Sum:", sum_result)



print("\n------------------------------------------------\n")

print("2. Basic Function without parameters")
def SayHello():
    print("Hello")
    
# Call the function
SayHello()



print("\n------------------------------------------------\n")

print("3. Function Default Arguments")

def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message

# Call the function
greeting_msg = greet("John")
print(greeting_msg)



print("\n------------------------------------------------\n")

print("4. Function with *args (Variable Number of Arguments)")
def print_args(*args):
    for arg in args:
        print(arg)

# Call the function
print_args(1, "two", 3.0, [4, 5])




print("\n------------------------------------------------\n")

print("5. Function with **kwargs (Keyword Arguments)")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function
print_kwargs(name="John", age=25, city="New York")



print("\n------------------------------------------------\n")

print("6. Lambda Function")
multiply = lambda x, y: x * y
result = multiply(4, 5)
print("Product:", result)



print("\n------------------------------------------------\n")

print("7. Recursive Function")
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")



print("\n------------------------------------------------\n")

print("8.Local and Global Variables")
print("8.1.Local Variable")
global_var = 20  # This is a global variable

def example_function():
    print(global_var)  # Accessing the global variable within the function

example_function()
print(global_var)  # Accessing the global variable outside the function


print("8.1.Global Variable")
global_var = 20  # This is a global variable

def modify_global():
    global global_var
    global_var += 5

modify_global()
print(global_var)  # The value of the global variable has been modified by the function



print("\n------------------------------------------------")

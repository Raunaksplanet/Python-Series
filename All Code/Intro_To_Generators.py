'''
Introduction to 
Generators
'''

print("------------------------------------------------\n")

print("1. Simple Generator")

def simple_generator():
    for i in range(5):
        yield i

# Create a generator object
gen = simple_generator()

# Iterate over the generator
print(next(gen))
print(next(gen))
print(next(gen))

print("\n------------------------------------------------\n")


print("2. Simple Generator using loop")

def simple_generator():
    for i in range(5):
        yield i

# Create a generator object
gen = simple_generator()

# Iterate over the generator
for i in gen:
    print(i)

print("\n------------------------------------------------\n")

print("3. fibonacci using Generator")
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Create a generator object
fib_gen = fibonacci_generator(5)

# Iterate over the generator
for number in fib_gen:
    print(number)

print("\n------------------------------------------------")

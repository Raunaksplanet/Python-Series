'''
Introduction to 
Iterators
'''

print("------------------------------------------------\n")

print("1st Simple Iteration")
string = "GFG"
char = iter(string)
 
print(next(char))
print(next(char))
print(next(char))


print("\n------------------------------------------------\n")

print("2nd Simple Iteration")
iterator = iter(range(1, 4))

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break


print("\n------------------------------------------------")

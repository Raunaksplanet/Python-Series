print("---------------------------------------")
# Iterating over a list
l = ["geeks", "for", "geeks"]
 
for i in l:
    print(i)

print("---------------------------------------")


# Iterating over dictionary
print("Dictionary Iteration")
 
d = dict()
 
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))


print("---------------------------------------")

# Iterating over a String
print("String Iteration")
 
s = "Geeks"
for i in s:
    print(i)

print("---------------------------------------")

for i in range(-5, 2, 2):
    print("1st loop ",i)

print("---------------------------------------")

for i in range(-5, 2):
    print("2nd loop ",i)

print("---------------------------------------")


for i in range(10):
    print("3rd loop ",i)

print("---------------------------------------")


fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

print("---------------------------------------")

# Prints all letters except 'e' and 's'
 
for letter in 'geeksforgeeks':
 
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

print("---------------------------------------")

n = 1
while n < 11:
    print(n*3)
    n = n + 1

print("---------------------------------------")

print("---------------------------------------\n")
# Introduction to List

n = [1,2,3,4,"raunak",4.44,1]

for i in n:
    print(i)

'''
Same Output
for i in range(0,7,2):
    print(n[i])

    
print(n[0:7:2])
'''

print("\n---------------------------------------\n")


print(n[0:7:2])


print("\n---------------------------------------\n")


nn = [1,2,3,4,5,6,7,8]
print("Printing list: ", nn)
print("\n")
print("Printing list without last element: ", nn[0:-1])
print("\n")
print("Printing list with jumping single element: ", nn[::2])
print("\n")
print("Printing list in Reverse: ", nn[::-1])
print("\n")

print("\n---------------------------------------\n")

lst = [ i for i in range(1,11)]
print("list Comprehension: ",lst)

print("\n")

lst = [i for i in range(1,11) if i % 2 == 0]
print("list Comprehension: ",lst)

print("\n---------------------------------------\n")

print("List Operations/Built in Method")
# Creating list
my_list = [1, 2, 3, 'apple', 'banana', 3.14, True]
print(my_list)

# Accessing list
first_element = my_list[0]
third_element = my_list[2]
print(first_element)  # Output: 1
print(third_element)  # Output: 3

# Subset list
subset = my_list[1:4]
print(subset)  # Output: [2, 3, 'apple']

# Concatenate list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 'a', 'b', 'c']

# Repeating list
repeated_list = [1, 2] * 3
print(repeated_list)  # Output: [1, 2, 1, 2, 1, 2]

# Checking elements in list
is_present = 'apple' in my_list
print(is_present)  # Output: True

# checking Length in list
list_length = len(my_list)
print(list_length)  # Output: 7

# Modifying element in list
my_list[0] = 100
print(my_list)  # Output: [100, 2, 3, 'apple', 'banana', 3.14, True]

# Append in list
my_list.append('grape')
print(my_list)  # Output: [100, 2, 3, 'apple', 'banana', 3.14, True, 'grape']

# Extend in list
new_elements = ['orange', 'kiwi']
my_list.extend(new_elements)
print(my_list)  # Output: [100, 2, 3, 'apple', 'banana', 3.14, True, 'grape', 'orange', 'kiwi']

# Remove in list
my_list.remove('banana')
print(my_list)  # Output: [100, 2, 3, 'apple', 3.14, True, 'grape', 'orange', 'kiwi']

# Delete in list
del my_list[1]
print(my_list)  # Output: [100, 3, 'apple', 3.14, True, 'grape', 'orange', 'kiwi']

# Index in list
my_list = [10, 20, 30, 20, 40]
index = my_list.index(20)
print(index)  # Output: 1

# Sort in list
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

# Reverse in list
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

print("\n---------------------------------------")

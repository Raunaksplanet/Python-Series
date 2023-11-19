'''
Introduction to 
File Handling
'''

print("------------------------------------------------\n")

# 1.Reading
file = open("File.txt", "r")  # "r" stands for read mode

# file = open("File.txt", "w")  # "w" stands for Write mode

# file = open("File.txt", "a")  # "a" stands for Append mode

# file = open("File.txt", "a+")  # "a" stands for Append and read mode

# file = open("File.txt", "r+")  # "a" stands for Read and Write mode

# file = open("File.txt", "w+")  # "a" stands for Write and Read mode

# 2.Closing
# file.close()

print("\n------------------------------------------------\n")

# 3.Write a file
# 3.1. Open a file with write mode
file = open("file.txt", "r+")
file.write("Hello there, im under the water")
cc = file.readline()
print(cc)
file.close

# 3.1. Open a file with write mode

file = open("file.txt", "a+")
file.write("\nHello there, im under the water\n")
cc = file.readline()
print(cc)
file.close



print("\n------------------------------------------------\n")

# content = file.read()
# content = file.readline()
# content = file.readlines()

# print(content)

file.close()
print("\n------------------------------------------------")

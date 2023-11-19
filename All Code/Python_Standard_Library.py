'''
Introduction to 
Python Standard Library
'''

print("------------------------------------------------\n")

print("1.Math Module")
import math

result = math.sqrt(25)
print(result)  

print(math.pi)      # Output: 3.141592653589793
print(math.e)       # Output: 2.718281828459045

result_ceil = math.ceil(4.3)
result_floor = math.floor(4.9)
print(result_ceil, result_floor)  # Output: 5 4

result = math.pow(2, 3)  # 2 raised to the power of 3
print(result)  # Output: 8.0

result = math.gcd(48, 18)
print(result)  # Output: 6

result = math.fabs(-7.25)
print(result)  # Output: 7.25




print("\n------------------------------------------------\n")

print("2.DateTime Module")
from datetime import datetime, date, time


current_datetime = datetime.now()
print(current_datetime)

# Creating a date object
my_date = date(2023, 11, 18)
print(my_date)  # Output: 2023-11-18

# Creating a time object
my_time = time(15, 30, 0)
print(my_time)  # Output: 15:30:00

my_datetime = datetime(2023, 11, 18, 15, 30, 0)
print(my_datetime)  # Output: 2023-11-18 15:30:00

formatted_date = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Output: 2023-11-18 15:30:00


print("\n------------------------------------------------\n")

print("3.Random Module")
import random
random_number = random.randint(1, 10)  # Random integer between 1 and 10 (inclusive)
print(random_number)

random_float = random.random()  # Random float between 0 and 1
print(random_float)

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)  # Get 3 unique elements
print(random_sample)

random_boolean = random.choice([True, False])
print(random_boolean)

print("\n------------------------------------------------")

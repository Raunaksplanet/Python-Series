'''
Introduction to 
Exception Handeling

'''

print("------------------------------------------------\n")

print("1.Try and Except Statements")
try:
    a = 5 / 0
except Exception as e:
    print("There is some error: ", e)


a = [1, 2, 3] 
try:  
    print ("Second element = %d" %(a[1])) 
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3])) 
except Exception as e: 
    print ("An error occurred: ", e) 



print("\n------------------------------------------------\n")

print("2.Try with else Statements")

try:
    print("Number is ", 5+5+12)
except:
    print("Exception occured")
else:
    print("No Exception occured")



print("\n------------------------------------------------\n")

print("3.Try with finally Statements")

try:
    print("Number is ", 5+5+12)
except:
    print("Exception occured")
else:
    print("No Exception occured")
finally:
    print("This line will always print")



print("\n------------------------------------------------")

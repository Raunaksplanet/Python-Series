a = 5
if(a == 5):
    a = a + 5 
    print("if Block", a)
elif(a == 10):
    print(a)
else:
    print("else Block")



# if..else chain statement 
letter = "A"
 
if letter == "B":
  print("letter is B")
   
else: 
     
  if letter == "C":
    print("letter is C")
     
  else:
       
    if letter == "A":
      print("letter is A")
       
    else: 
      print("letter isn't A, B and C")


# if-elif statement example
 
letter = "A"
 
if letter == "B":
    print("letter is B")
 
elif letter == "C":
    print("letter is C")
 
elif letter == "A":
    print("letter is A")
 
else:
    print("letter isn't A, B or C")



# python program to illustrate nested If statement
 
i = 10
if (i == 10):
    i += 5
    if (i < 15):
        print("i is smaller than 15")

    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

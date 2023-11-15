print("---------------------------------------")
# Jumping Statements
# 1.Break
print("Break Statement Example")

for i in range(1,10):
    if(i==5):
        break
    else:
        print(i)

print("---------------------------------------")
# Jumping Statements
# 2.Continue
print("Continue Statement Example")

for i in range(1,10):
    if(i==5):
        print("Number is Skipped due to Continue statement")
        continue
    else:
        print(i)


print("---------------------------------------")
# Jumping Statements
# 3.pass

print("Pass Statement Example")
for i in range(1,10):
    if(i==5):
        print("Number is Skipped due to Continue statement")
        pass
    else:
        print(i)

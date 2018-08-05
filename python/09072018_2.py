x = int(input("enter max limit >>> "))

a = 0
b = 1
c = 0
z = 1

print(str(a) + "\n" + str(b))
while True :
    c = a + b
    a = b
    b = c
    if c > x :
        print("fibonacci series over")
        break
    else:
        print(c)
        z = z * c

print("factorial is === " + str(z))
        
   
    

a , b = 0 , 1
x = int(input("max > "))
while a <= x:
    b = a + b
    a , b = b , a
    print(b)

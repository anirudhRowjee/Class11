#write a program to display the prime numbers in a given range

a = int(input("please enter start of range"))
b = int(input("please enter end of range"))

for i in range(a, b+1):
    for j in range(2, (i-1)):
        if i % j == 0:
            break
    else:
        print(i, "is prime")

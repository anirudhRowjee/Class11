n1 = int(input("number 1\n"))
n2 = int(input("number 2\n"))
n3 = int(input("number 3\n"))

s = n1 + n2 + n3
print("sum of all is " + str(s))

if n1 == n2 == n3 :
    print("sum w/o repeats is 0")
elif n1 == n2 :
    print("sum w/o repeats is -- " + str(n1 + n3))
elif n2 == n3 :
    print("sum w/o repeats is -- " + str(n1 + n3))
elif n1 == n3 :
    print("sum w/o repeats is -- " + str(n1 + n2))



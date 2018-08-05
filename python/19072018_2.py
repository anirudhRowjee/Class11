#find hcf and lcm of two numbers

x = int(input("please enter first number"))
y = int(input("please enter second number"))

xfactorlist = []
yfactorlist = []
commonfactorlist = []

for i in range(1, x+1):   # find all factors of x
    if x % i == 0:
        xfactorlist.append(i)

for i in range(1, y+1):     #find all factors of y
    if y % i == 0:
        yfactorlist.append(i)

for s in xfactorlist:
    for d in yfactorlist:   #find all common factors
        if s == d :
            commonfactorlist.append(s)

hcf = commonfactorlist[len(commonfactorlist) - 1] # hcf

lcm = ((x * y) / hcf) #x*y = lcm * hcf

print("hcf is >>>>>>> ", hcf)
print("lcm is >>>>>>> ", lcm)


'''

x = int(input("number 1"))
y = int(input("number 2"))

lcm = 0

for i in range(1, ((x*y) + 1)):
    if i % x == 0 and i % y == 0 :
        print("lcm is ", i)
        lcm = i
        break

hcf = ((x*y)/lcm)
print("hcf is ", hcf)

'''

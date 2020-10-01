
"""
i used for loop for taking multiple values.
one = input("number 1 \n")
two = input("number 2 \n")
three = input("number 3 \n")

x = [] (intialies this empty list in the starting)

x.append(one)
x.append(two)
x.append(three)

x.sort()
y = len(x) (no need of this  as we can use negative indexing)

print "smallest number is " + str(x[0])
print "largest is " + str(x[y -1])"""

x = []
for i in range(0, 3):
    y = int(input("enter three numbers each followed by an 'Enter'"))
    x.append(y)
x.sort()

print("smallest number is ", x[0])
print("largest is ", x[-1])

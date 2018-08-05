
##one = input("number 1 \n")
##two = input("number 2 \n")
##three = input("number 3 \n")
##
##x = []
##
##x.append(one)
##x.append(two)
##x.append(three)
##
##x.sort()
##y = len(x)
##
##print "smallest number is " + str(x[0])
##print "largest is " + str(x[y -1])

x = list(input("enter a list of numbers, separated by commas"))
x.sort()
y = len(x)
print "smallest number is " + str(x[0])
print "largest is " + str(x[y - 1])

import random
z = random.randint(1, 10)
c = 1

print("TESTING : number is " + str(z) + "\n")
while c <= 5:
    print("attempt " + str(c) +"/5" )
    x = int(input("pls enter a number between 1, 10 >> \n"))
    if x == z:
        print("Successful Guess!")
        break
    else:
        print("unsuccessful try \n")
        c += 1

if c >= 6:
    print("Sorry! Number was " + str(z))

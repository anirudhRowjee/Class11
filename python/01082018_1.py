while True:
    x = input("Please enter a word >>> ")
    x_l = x.lower()
    revstr = ""
    for i in range(len(x), 0, -1):
        revstr = revstr +  x_l[i-1]
    if revstr == x_l:
        print("phrase is palindrome")
    else:
        print("phrase is not a palindrome")

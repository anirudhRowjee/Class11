#take word and check the following : 1) palindrome 2)valid gmail address

x = input("give word")

if x == x[::-1]:
    print(x, "Is a palindrome")
else:
    print(x, "is not palindrome")

if x.find("@") != -1 and x.find(".com") != -1:
    print("I will send you my mixtape")


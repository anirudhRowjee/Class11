x = input("give sentence bro")
words = 1
upper_letters = 0
lower_letters = 0
digits = 0
letter  = 0

for i in x:
    if i.isupper() == True:
        upper_letters = upper_letters + 1
    elif i.islower() == True:
        lower_letters = lower_letters + 1
    elif i.isdigit() == True:
        digits = digits + 1
    if i == " " :
        words = words + 1


print("there are ",words, " words")
print("there are ",upper_letters, " uppercase letters")
print("there are ",lower_letters, " lowercase letters")
print("there are ",digits, " numbers")
print("the reverse of the sentence is ", x[::-1])

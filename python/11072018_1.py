"""for i in ("Hello"):
    print("(" + i + ")")
    for j in [3, 7, 12, 18]:
        if j > 7:
            break
        print(j)"""

x = list(input("Enter a series of Numbers"))
print(x)
op = ("+", "-", "*", "/")

for i in x:
    for j in x:
        for k in op:
            problem_statement = str(i) + k + str(j)
            ans = eval(problem_statement)
            print("The Answer for " + problem_statement + " is " + str(ans))

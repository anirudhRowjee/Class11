while True:
    x = input("please enter a sentence >>> ").lower()
    al = "abcdefghijklmnopqrstuvwxyz"

    l_present = ""
    l_absent = ""

    for i in al:
        count = 0
        for j in x:
            if i == j :
                count += 1
        if count > 0 :
            l_present = l_present + i
        if count == 0 :
            l_absent = l_absent + i
        print(i,'=',count)

    print("Letters present = ", l_present)
    print("Letters absent = ", l_absent)


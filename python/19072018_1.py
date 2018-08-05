while True:
    p = int(input("give number of rows"))
    y = input("give character to be printed")
    x = p // 2
    for i in range(1, (x+ 1)):
        s = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        s.insert((i - 1), y)
        c = "".join(s)
        print(c[::-1], c)
    for i in range((x+ 1), 0, -1):
        s = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        s.insert((i - 1), y)
        c = "".join(s)
        print(c[::-1], c)
        
        
        

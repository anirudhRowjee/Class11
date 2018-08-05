while True:
    x = int(input("\npls give number >>> "))
    y = int(input("\nenter 2 for binary, 8 for octadecimal, 16 for hexadecimal and 3 for all >>> "))

    while type(x) is int and type(y) is int:
        c = ""
        if y == 2:    #binary calculation
            while x >= 1:
                d = x % 2
                c = str(d) + c
                x = x // 2
            print('\nbinary equivalent is ', str(c))
            break
        if y == 8:  #octal calculation
            while x >= 1:
                d = x % 8
                c = str(d) + c
                x = x // 8
            print('\noctadecimal equivalent is ', str(c))
            break
        if y == 16: #hexadecimal calculation
            while x >= 1:
                d = x % 16
                if d >= 10 :
                    if d == 10:
                        c = 'A' + c
                    if d == 11:
                        c = 'B' + c
                    if d == 12:
                        c = 'C' + c
                    if d == 13:
                        c = 'D' + c
                    if d == 14:
                        c = 'E' + c
                    if d == 15:
                        c = 'F' + c
                else:
                    c = str(d) + c
                x = x // 16
            print('\nhex equivalent is ', str(c))
            break
        if y == 3:
            b = ""
            o = ""
            h = ""
            bx = x
            ox = x
            hx = x
            while bx >= 1:
                d = bx % 2
                b = str(d) + b
                bx = bx // 2
            print('\tbinary equivalent is >>>>>>', str(b))
            while ox >= 1:
                d = ox % 8
                o = str(d) + o
                ox = ox // 8
            print('\toctadecimal equivalent is >>>>>>', str(o))
            while hx >= 1:
                d = hx % 16
                if d >= 10 :
                    if d == 10:
                        h = 'A' + h
                    if d == 11:
                        h = 'B' + h
                    if d == 12:
                        h = 'C' + h
                    if d == 13:
                        h = 'D' + h
                    if d == 14:
                        h = 'E' + h
                    if d == 15:
                        h = 'F' + h
                else:
                    h = str(d) + h
                hx = hx // 16
            print('\tthe hex equivalent is >>>>>>', str(h))
            break
    else:
        print("<<<-------PLEASE GIVE VALID INTEGER INPUT------->>>")
    


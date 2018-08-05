while True:
    u_choice = input('1 for c2f, 2 for f2c, 3 for exit \n')
    if u_choice == 1:
        temp_c = input('Enter temp in Celsius \n')
        temp_f = (9/5)*int(temp_c) + 32
        print 'your temp in farenheit is ' + str(temp_f)
    if u_choice == 2:
        temp_fa = input('Enter temp in Farenheit \n')
        temp_ca = (int(temp_fa) - 32) * 5/9
        print 'your temp in celsius is ' + str(temp_ca)
    if u_choice == 3:
        break

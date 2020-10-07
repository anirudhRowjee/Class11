while True:
    u_choice = input('1 for c2f, 2 for f2c, 3 for exit \n')
    if u_choice == 1:
        temp_c = float(input('Enter temp in Celsius \n'))
        temp_f = (9/5)* temp_c + 32
        print (f"your temp in celsius is {temp_f}")
    if u_choice == 2:
        temp_fa = float(input('Enter temp in Farenheit \n'))
        temp_ca = (temp_fa - 32) * 5/9
        print (f"your temp in celsius is {temp_f}")
    if u_choice == 3:
        break

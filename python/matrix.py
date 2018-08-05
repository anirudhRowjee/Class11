
# program to accept matrices from user, transpose and multiply matrices

while True:
    print("\nprogram to accept matrices and perform transpose, multiplication by rowjee")
    rn = int(input("please give number of rows/columns in the square matrices >>> "))

    m1 = []
    m2 = []
    tm1 = []
    tm2 = []
    m_final = []

    for i in range(1,3):        # iterator starts for number of matrices i.e. 2
        print("MATRIX NUMBER ", i)
        t = []                      # create temporary list for the matrix to exist in
        for j in range(1,rn+1):     # iterator starts for row data input
            r = []                  # create empty list for a row
            for a in range(1, rn+1):
                x = int(input("give element " + str(a) + " for row " + str(j) + " >>> ")) # take input for nth element for xth row
                r.append(x)   # append that to list; this allows for multiple digit integers with no constraint on input
            t.append(r) # append said row to the table
        if i == 1:
            m1 = t
        elif i == 2:
            m2 = t

    for i in range(1,3):
        if i == 1:
            print("\nMATRIX ONE")
            for j in range(1, len(m1) + 1):
                print(m1[j-1])
        if i == 2:
            print("\nMATRIX TWO")
            for j in range(1, len(m2) + 1):
                print(m2[j-1])


    # transpose, let's do this

    for i in range(1,3):
        if i == 1:
            t = m1
            t_n = []
            for a in range(1, len(t)+1):        # iterator for column
                r = []
                for b in range(1, len(t)+ 1):   # iterator for row
                    x = t[b-1][a-1]
                    r.append(x)
                t_n.append(r)
            tm1 = t_n
        if i == 2:
            t = m2
            t_n = []
            for a in range(1, len(t)+1):        # iterator for column
                r = []
                for b in range(1, len(t)+ 1):   # iterator for row
                    x = t[b-1][a-1]
                    r.append(x)
                t_n.append(r)
            tm2 = t_n

    print("\n")

    for i in range(1,3):
        print("\n")
        if i == 1:
            print("TRANSPOSED MATRIX 1")
            for j in range(1, len(tm1) + 1):
                print(tm1[j-1])
        if i == 2:
            print("TRANSPOSED MATRIX 2")
            for j in range(1, len(tm2) + 1):
                print(tm2[j-1])

    # matrix multiplication

    # instead of doing over-complicated algorithmic nightmares,
    # use transpose of matrix two to make multiplication easier

    temp_ml = []
    op_1 = m1
    op_2 = tm2

    for r_m1 in range(1,len(op_1)+1):    # row count for matrix one
        tr = []
        for r_tm2 in range(1, len(op_2)+1): # row count for matrix two
            s = 0
            for i_m in range(1, len(op_1)+1): # index count in both lists as l2 is transposed
                s += op_1[r_m1-1][i_m-1] * op_2[r_tm2-1][i_m-1]
            tr.append(s)
        temp_ml.append(tr)

    print("\nMATRICES MULTIPLIED")
    for i in range(1, len(temp_ml)+1):
        print(temp_ml[i-1])
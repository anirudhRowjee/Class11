b = [["*", "*", "*"],["*", "*", "*"],["*", "*", "*"]]

def print_board(board):
    print("\n")
    print("\t"," " ,1, 2, 3, "\n")
    for i in range(0,3):
        print("\t",i+1, board[i][0], board[i][1], board[i][2], "\n")

def win_check(board):
    if board[0][0] == board[0][1] == board[0][2] == "x" or board[0][0] == board[0][1] == board[0][2] == "o" :
        return True
    elif board[1][0] == board[1][1] == board[1][2] == "x" or board[1][0] == board[1][1] == board[1][2] == "o" :
        return True
    elif board[2][0] == board[2][1] == board[2][2] == "x" or board[2][0] == board[2][1] == board[2][2] == "o" :
        return True
    elif board[0][0] == board[1][0] == board[2][0] == "x" or board[0][0] == board[1][0] == board[2][0] == "o" :
        return True
    elif board[0][1] == board[1][1] == board[2][1] == "x" or board[0][1] == board[1][1] == board[2][1] == "o" :
        return True
    elif board[0][2] == board[1][2] == board[2][2] == "x" or board[0][2] == board[1][2] == board[2][2] == "o" :
        return True
    elif board[0][0] == board[1][1] == board[2][2] == "x" or board[0][0] == board[1][1] == board[2][2] == "o" :
        return True
    elif board[0][2] == board[1][1] == board[2][0] == "x" or board[0][2] == board[1][1] == board[2][0] == "o" :
        return True
    else:
        return False

print_board(b)

def make_play(board, count):
    if count > 9:
        print("GAME OVER!!!")
        exit()
    if win_check(board) == True:
        print("YOU WON")
        exit()
    else:
        if count % 2 == 0:
            ch = "x"
            print("TURN >>>> X")
        if count % 2 != 0:
            ch = "o"
            print("TURN >>>> O")
        x = int(input("x co-ordinate b/w 1-3"))
        y = int(input("y co-ordinate b/w 1-3"))
        x = x- 1
        y = y -1
        board[y][x] = ch
        print_board(board)

        

for i in range(0, 9):
    make_play(b, i)
    

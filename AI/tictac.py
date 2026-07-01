import math

board = [" " for i in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):

    win_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for position in win_positions:
        if board[position[0]] == player and board[position[1]] == player and board[position[2]] == player:
            return True

    return False

def board_full():
    return " " not in board

def minimax(is_ai):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_ai:

        best = -math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                if score > best:
                    best = score

        return best

    else:

        best = math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                if score < best:
                    best = score

        return best

def ai_move():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def player_move():

    while True:

        try:
            move = int(input("Enter position (1-9): "))

            if move >= 1 and move <= 9:

                if board[move-1] == " ":
                    board[move-1] = "X"
                    break

                else:
                    print("Position already occupied.")

            else:
                print("Enter number between 1 and 9.")

        except:
            print("Invalid input.")

print("===================================")
print(" TIC TAC TOE AI ")
print(" You = X")
print(" Computer = O")
print("===================================")

print_board()

while True:

    player_move()

    print_board()

    if check_winner("X"):
        print("You Win!")
        break

    if board_full():
        print("Match Draw!")
        break

    print("Computer is thinking...")

    ai_move()

    print_board()

    if check_winner("O"):
        print("Computer Wins!")
        break

    if board_full():
        print("Match Draw!")
        break

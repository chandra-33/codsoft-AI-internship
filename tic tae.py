import math
def initialize_board():
    return [" " for _ in range(9)]
def print_board(board):
    print("\n")
    for row in range(3):
        print(f" {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} ")
        if row < 2:
            print("---|---|---")
    print("\n")
def check_winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]              
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] != " ":
            return board[pos[0]]
    if " " not in board:
        return "Draw"
    return None
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif winner == "Draw":
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def find_best_move(board):
    best_value = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_value = minimax(board, 0, False)
            board[i] = " "
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move
def tic_tac_toe():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'.")
    print_board(board) 
    while True:
        while True:
            try:
                user_move = int(input("Enter your move (1-9): ")) - 1
                if board[user_move] == " ":
                    board[user_move] = "X"
                    break
                else:
                    print("Invalid move!")
            except (IndexError, ValueError):
                print("Invalid input!Enter a number between 1 and 9.")
        
        print_board(board)
        if check_winner(board):
            winner = check_winner(board)
            if winner == "X":
                print("Congratulations! You win!")
            elif winner == "Draw":
                print("It's a draw!")
            else:
                print("AI wins!")
            break
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move] = "O"
        print_board(board)
        if check_winner(board):
            winner = check_winner(board)
            if winner == "O":
                print("AI wins! Better luck next time.")
            elif winner == "Draw":
                print("It's a draw!")
            break
tic_tac_toe()

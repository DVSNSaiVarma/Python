def draw_board(board):
    print("   |   |")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |")

def make_move(board, player, move):
    board[move] = player

def has_won(board, player):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in win_positions:
        if board[pos[0]] == player and board[pos[1]] == player and board[pos[2]] == player:
            return True
    return False

def main():
    board = [" " for x in range(9)]
    draw_board(board)
    player = "X"
    while True:
        move = int(input("Enter your move (0-8): "))
        make_move(board, player, move)
        if has_won(board, player):
            print("Player {} has won!".format(player))
            break
        draw_board(board)
        if player == "X":
            player = "O"
        else:
            player = "X"

main()

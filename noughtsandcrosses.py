import random


def draw_board(board):
    print('   |   |')
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print('   |   |')


def display_welcome(board):
    print("Welcome to Tic-Tac-Toe!")
    board = initialize_board(board)
    draw_board(board)


def initialize_board(board):
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board


# def initialize_board(board):
#     # return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#     return board


def get_player_move(board):
    while True:
        # Get the player's move as a tuple of (row, col)
        move = input("Enter your move in the form 'row col': ")
        try:
            row, col = map(int, move.strip().split())
            # Check if the move is valid
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            print("Invalid input. Please enter your move in the form 'row col'.")


def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == len(row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board) - i - 1] == player for i in range(len(board))):
        return True

    return False


def check_draw(board):
    # Check if all cells are filled and no one has won
    if all(all(cell != ' ' for cell in row) for row in board):
        return True
    return False


# This is computer as opponent
# def play_game():
#     board = initialize_board()
#     player = 'X'
#     computer = 'O'
#     current_player = player
#     while True:
#         draw_board(board)
#         if current_player == player:
#             print(f"{current_player}'s turn")
#             row, col = get_player_move(board)
#         else:
#             print(f"{current_player}'s turn")
#             row, col = get_computer_move(board)
#         board[row][col] = current_player
#         if check_win(board, current_player):
#             draw_board(board)
#             print(f"{current_player} has won the game!")
#             break
#         elif check_draw(board):
#             draw_board(board)
#             print("The game is a draw!")
#             break
#         else:
#             current_player = computer if current_player == player else player


# Here we save the winner in the leader boards-file
def play_game(board):
    board = initialize_board(board)
    player = 'X'
    computer = 'O'
    current_player = player
    scores = {}
    while True:
        draw_board(board)
        if current_player == player:
            print(f"{current_player}'s turn")
            row, col = get_player_move(board)
        else:
            print(f"{current_player}'s turn")
            row, col = get_computer_move(board)
        board[row][col] = current_player
        if check_win(board, current_player):
            draw_board(board)
            print(f"{current_player} has won the game!")
            if current_player == player:
                name = input("Enter your name: ")
                scores[name] = 1
                store_scores(scores)
            break
        elif check_draw(board):
            draw_board(board)
            print("The game is a draw!")
            break
        else:
            current_player = computer if current_player == player else player


def get_computer_move(board):
    """
    Returns a randomly chosen cell from the board
    """
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)


# This is multiplayer code
# def play_game(board):
#     # board = initialize_board()
#     player_1 = 'X'
#     player_2 = 'O'
#     current_player = player_1
#     while True:
#         draw_board(board)
#         print(f"{current_player}'s turn")
#         row, col = get_player_move(board)
#         board[row][col] = current_player
#         if check_win(board, current_player):
#             draw_board(board)
#             print(f"{current_player} has won the game!")
#             break
#         elif check_draw(board):
#             draw_board(board)
#             print("The game is a draw!")
#             break
#         else:
#             current_player = player_2 if current_player == player_1 else player_1

def display_menu():
    print("1. Play game")
    print("2. Save score to leaderboard.txt")
    print("3. Load and display scores from leaderboard.txt")
    print("q. Quit")


def menu():
    choice = input("Enter your choice: ")
    return choice


def load_scores():
    file_path = 'leaderboards.txt'
    scores = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                name, score = line.strip().split(',')
                scores[name] = int(score)
    except FileNotFoundError:
        print("File not found")
    return scores


# def store_scores(scores):
#     file_path = "leaderboards.txt"
#     with open(file_path, 'w') as f:
#         for name, score in scores.items():
#             f.write(f"{name},{score}\n")


def store_scores(scores):
    file_path = 'leaderboards.txt'
    with open(file_path, 'w') as f:
        for name, score in scores.items():
            f.write(f"{name},{score}\n")


def display_leaderboard(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores):
        print(f"{i + 1}. {name}: {score}\n")

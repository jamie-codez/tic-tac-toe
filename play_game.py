from noughtsandcrosses import *


def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    scores = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            play_game(board)
        elif choice == '2':
            name = input("Enter your name: ")
            score = input("Enter your score: ")
            scores[name] = int(score)
            store_scores(scores)
        elif choice == '3':
            scores = load_scores()
            display_leaderboard(scores)
        elif choice == 'q':
            print('Thank you for playing the "Unbeatable knots and crosses" game \nGoodbye')
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

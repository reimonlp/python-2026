import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        choice = input("""Games:
1. Hangman
2. Reversegam
3. Tic Tac Toe
0. Exit
Select an option: """)
        match choice:
            case "1":
                from hangman import playGame
                playGame()
            case "2":
                from reverse import playGame
                playGame()
            case "3":
                from tictactoe import playGame
                playGame()
            case "0":
                break

if __name__ == "__main__":
    main()
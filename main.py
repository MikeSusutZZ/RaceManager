def main_menu():
    print("Welcome to the Racing Game!")
    print("1. New Game")
    print("2. Load Game")

    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        # New Game
        start_new_game()
    elif choice == "2":
        # Load Game
        load_game()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_new_game():
    # Code for starting a new game
    print("Starting a new game...")
    upgrades = 2
    teamName = input("Enter team name: ")


def load_game():
    # Code for loading a game
    print("Loading a game...")

# Starting point of the program
main_menu()

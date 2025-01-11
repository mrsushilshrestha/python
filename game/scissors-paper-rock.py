import random

class RockPaperScissors:
    def __init__(self, user_input):
        self.user_input = user_input
        self.computer = random.choice(["scissors", "paper", "rock"])
        print(f"\nYour Input: {self.user_input}\nComputer Input: {self.computer}")

    def play_game(self):
        if self.user_input == self.computer:
            print("It's a Tie!")
        elif (self.user_input == 'scissors' and self.computer == 'paper') or \
             (self.user_input == 'rock' and self.computer == 'scissors') or \
             (self.user_input == 'paper' and self.computer == 'rock'):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

def get_user_choice():
    while True:
        message = """
        Choose an option:
        1. Scissors
        2. Paper
        3. Rock
        4. Exit
        """
        user_input = input(message).strip()
        if user_input == '1':
            return 'scissors'
        elif user_input == '2':
            return 'paper'
        elif user_input == '3':
            return 'rock'
        elif user_input == '4':
            return None
        else:
            print("Invalid option! Please enter 1, 2, 3, or 4.")

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Exiting the game. Goodbye! 👋")
            break

        game = RockPaperScissors(user_choice)
        game.play_game()

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ('yes', 'y'):
            print("Thank you for playing! See you next time! 🎮")
            break

if __name__ == "__main__":
    main()

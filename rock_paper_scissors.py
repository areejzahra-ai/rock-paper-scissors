"""Rock Paper Scissors - a command-line game built with Python.

Features:
- Play against the computer
- Choose how many rounds to play
- Live scoreboard
- Input validation
- Play again option"""

import random

CHOICES = {"r": "Rock", "p": "Paper", "s": "Scissors"}

# Each key beats its value
WINS_AGAINST = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

def get_player_choice():
    """Ask the player for a valid choice."""
    while True:
        pick = input("Choose [r]ock, [p]aper, or [s]cissors: ").strip().lower()
        if pick in CHOICES:
            return CHOICES[pick]
        print("Invalid choice. Please enter r, p, or s.\n")
def get_rounds():
    """Ask how many rounds to play."""
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds > 0:
                return rounds
            print("Please enter a number greater than 0.\n")
        except ValueError:
            print("Please enter a valid number.\n")
def decide_winner(player, computer):
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if WINS_AGAINST[player] == computer:
        return "player"
    return "computer"
def play_game():
    """Play one full game (multiple rounds)."""
    rounds = get_rounds()
    player_score = 0
    computer_score = 0
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} of {rounds} ---")
        player = get_player_choice()
        computer = random.choice(list(CHOICES.values()))

        print(f"You:      {[player]} {player}")
        print(f"Computer: {[computer]} {computer}")

        result = decide_winner(player, computer)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    print("\n===== FINAL RESULT =====")
    print(f"You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations, you won the game!")
    elif computer_score > player_score:
        print("The computer won the game. Better luck next time!")
    else:
        print("The game is a draw!")
def main():
    print("=" * 30)
    print("  ROCK PAPER SCISSORS GAME")
    print("=" * 30)

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
if __name__ =="__main__":
    main()

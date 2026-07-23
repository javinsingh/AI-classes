import random
from colorama import Fore, init

init(autoreset=True)

options = ["rock", "paper", "scissors"]


def ai_move():
    ai_choice = random.choice(options)
    print(Fore.CYAN + f"AI chose: {ai_choice}")
    return ai_choice


def player_move():
    while True:
        player_choice = input(Fore.CYAN + "Enter your move (rock, paper, or scissors): ").lower()

        if player_choice in options:
            return player_choice

        print(Fore.RED + "Invalid move. Please enter rock, paper, or scissors.")


def check_game(ai_choice, player_choice):
    if ai_choice == player_choice:
        print(Fore.YELLOW + "It's a tie!")
        return True

    elif (
        (ai_choice == "rock" and player_choice == "scissors") or
        (ai_choice == "paper" and player_choice == "rock") or
        (ai_choice == "scissors" and player_choice == "paper")
    ):
        print(Fore.RED + "The AI won!")
        return False

    else:
        print(Fore.GREEN + "You won!")
        return False


def game():
    print(Fore.CYAN + "Hi! I am a rock, paper, scissors AI.")
    player_name = input(Fore.CYAN + "Please enter your name: ")
    print(Fore.CYAN + f"Hello, {player_name}! Let's play rock, paper, scissors! You begin.")

    running = True

    while running:
        player_choice = player_move()
        ai_choice = ai_move()
        running = check_game(ai_choice, player_choice)


game()
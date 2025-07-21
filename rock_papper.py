import random

def get_user_choice():
    choice = input("\nChoose [rock, paper, scissors]: ").lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("❗ Invalid choice. Try again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")
    if result == "tie":
        print("🤝 It's a tie!")
    elif result == "user":
        print("🎉 You win!")
    else:
        print("😢 You lose!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock > Scissors | Scissors > Paper | Paper > Rock")

    while True:
        print(f"\n--- Round {round_number} ---")
        user = get_user_choice()
        computer = get_computer_choice()
        result = decide_winner(user, computer)

        display_result(user, computer, result)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\n📊 Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing! Final Score:")
            print(f"✅ You: {user_score} | 🤖 Computer: {computer_score}")
            break

        round_number += 1

# Start the game
play_game()

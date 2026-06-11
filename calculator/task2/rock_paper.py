import random

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")

while True:

    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You Win!")
            user_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You Win!")
            user_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You Win!")
            user_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1

    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break

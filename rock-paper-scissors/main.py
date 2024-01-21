import random
print("*** WELCOME TO ROCK PAPER SCISSORS ***")
player = input("\nSelect Rock, Paper, or Scissor :").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer selected: ", computer)

if player == "rock" and computer == "paper":
    print("\n*** Computer Won ***")
elif player == "paper" and computer == "scissor":
    print("\n*** Computer Won ***")
elif player == "scissor" and computer == "rock":
    print("\n*** Computer Won ***")
elif player == computer:
    print("\n*** It's a Tie ***")
else:
    print("\n*** Player Won ***")
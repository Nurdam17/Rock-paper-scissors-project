import random
print("How many rounds do you want?")
number_of_rounds=int(input())
count_win=0
count_lose=0

while count_win<=number_of_rounds or count_lose<=number_of_rounds:
    user_action=input("Enter your choice (rock, paper, scissors): ")
    possible_action=["rock", "paper", "scissors"]
    computer_action=random.choice(possible_action)

    print(f"\nYour choice: {user_action}, Computer choice: {computer_action}.\n")

    if user_action==computer_action:
        print("It's a tie)")

    elif user_action=="rock" and computer_action=="paper":
        print("Paper covers rock! You lose this round:(")
        count_lose+=1

    elif user_action=="rock" and computer_action=="scissors":
        print("Rock smashes scissors! You win this round!")
        count_win+=1

    elif user_action=="scissors":
        if computer_action=="rock":
            print("Rock smashes scissors! You lose this round:(")
            count_lose+=1

        elif computer_action=="paper":
            print("Scissors cuts paper! You win this round!")
            count_win+=1

    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win this round!")
            count_win+=1

        elif computer_action=="scissors":
            print("Scissors cuts paper! You lose this round:(")
            count_lose+=1

    if count_lose==number_of_rounds or count_win==number_of_rounds:
        break

print("")
print(str(count_win)+" : "+str(count_lose))
print("")
if count_win>count_lose:
    print("You are winner!")
else:
    print("Computer is winner")
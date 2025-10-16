import random
while True:
    user_action=input("Enter a choice(rock,paper scissors):")
    possible_action=["rock","paper","scissors"]
    computer_action=random.choice(possible_action)
    print(f"\nyou chose {user_action},computer chose{computer_action}.\n")

    if user_action==computer_action:
        print(f"both players selected {user_action} It is a tie")
    
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashes scissors you win")

        else:
            print("paper covers rock you lose")
    elif user_action=="paper":
        if computer_action=="scissors":
            print("scissors cuts paper you lose")
        else:
            print("paper covers rock you win")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors cuts paper you win")
        else:
            print("rock smashes scissors you lose")
    play_again=input("play again? (y/n):")
    if play_again=="y":
        break


    



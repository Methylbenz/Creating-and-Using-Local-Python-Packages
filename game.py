import random

comp_wins = 0
player_wins = 0

def choose_option():
        user_choice = input("choose Rock, Paper or scissors:")
        if user_choice in ["Rock", "rock", "r", "R"]:  
            user_choice = "r"
        elif user_choice in ["Paper","paper", "p", "P"]:
            user_choice = "p"
        elif user_choice in ["Scissors","scissors", "s", "S"]:
            user_choice = "s"
        else:
            print("try one more time")
            choose_option()
        return user_choice

def Computer_option():
        comp_choice = random.randint (1,3)
        if comp_choice ==1:
            comp_choice = "r"
        elif comp_choice ==2:
            comp_choice = "p"
        else:
            comp_choice ==3
            comp_choice = "s"
        return comp_choice

while True:
        print("")
        user_choice = choose_option()
        comp_choice = Computer_option()
        print("")

if user_choice == "r":
            if comp_choice == "r":
                print("You chose rock. The computer chose rock. it is a tie.")
            elif comp_choice == "p":
                print("You chose rock. The computer chose paper. you lose.")
                comp_wins += 1
            elif comp_choice == "s":
                print("You chose rock. The computer chose scissors. you win.")
                player_wins += 1

elif user_choice == "p":
            if comp_choice == "r":
                print("You chose paper. The computer chose rock.you win.")
                player_wins += 1
            elif comp_choice == "p":
                print("You chose paper. The computer chose paper. It is a tie.")
            elif comp_choice == "s":
                print("You chose paper. The computer chose scissors. you win.")
                comp_wins += 1

            elif user_choice == "s":
             if comp_choice == "r":
                print("You chose scissors. The computer chose rock.you lose.")
                comp_wins += 1
            elif comp_choice == "p":
                print("You chose scissors. The computer chose paper. you win.")
                player_wins += 1
            elif comp_choice == "s":
                print("You chose scissors. The computer chose scissors. It is a tie.")
                
print("")
print("player wins:" + str(player_wins))
print("comp_wins:" + str(comp_wins))
print("")

user_choice = input("Do you have the interest of playing again? (y/n)")
if user_choice is ["Y", "y", "yes", "Yes"]:
    print("continue")
elif user_choice is ["N", "n", "no", "No"]:
    raise Exception
else:
    raise Exception
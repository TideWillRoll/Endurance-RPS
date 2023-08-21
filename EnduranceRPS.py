import random
def play():
    choices = ('Rock', 'Paper', 'Scissors')
    user_choice = input(choices)
    computer_choice = random.choice(choices)
    is_win = (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper')
    is_loss = (user_choice == 'Rock' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Rock')
    tie = (user_choice == 'Rock' and computer_choice == 'Rock') or (user_choice == 'Paper' and computer_choice == 'Paper') or (user_choice == 'Scissors' and computer_choice == 'Scissors') 
    print(f"You chose {user_choice}, Computer chose {computer_choice}")
    player_score = 0
    computer_score = 0
    def score():
        print("You", player_score, "Computer", computer_score)
    if is_win:
        player_score += 1
        print("You won!")
        score()
        play()
    elif is_loss:
        computer_score += 1
        print("You lost! Better luck next time!")
        score()
        script()
    elif tie:
        player_score += 0; computer_score += 0
        print("That's a tie!")
        score()
        play()   
def script():
    restart = input("Play again?")
    if restart == "Yes" or restart == "yes":
        play()
        script()
    elif restart == "No" or restart == "no":
        print("Thanks for playing!")   
        quit()
play()
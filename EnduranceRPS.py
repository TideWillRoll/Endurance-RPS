import random
player_score = 0
computer_score = 0
def play():
    global player_score, computer_score
    choices = ('Rock', 'Paper', 'Scissors')
    user_choice = input(choices)
    computer_choice = random.choice(choices)
    is_win = (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper')
    is_loss = (user_choice == 'Rock' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Rock')
    tie = user_choice == computer_choice
    def score():
        print("You", player_score, "Computer", computer_score)
    if is_win:
        player_score += 1
        print("You won!")
        score()
        play()
    elif is_loss:
        if player_score > 0:
             player_score = 0 and computer_score == 0
        print("You lost! Better luck next time!")
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
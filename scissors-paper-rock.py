# "scissors-paper-rock"
import random

class Tiktak:
    def __init__(self,user_input):
            self.user_input = user_input
            self.computer = random.choice(["scissors", "paper", "rock"])
            print(f"Your Input: {self.user_input}\nComputer Input: {self.computer}")

    def game(self):
        #   print(self.computer)
        if self.user_input=='scissors' and self.computer=='paper':
            print("You win!!!")    
        elif self.user_input=='rock' and self.computer=='scissors':
            print("You win!!!")       
        elif self.user_input=='paper' and self.computer=='rock':
            print("You win!!!") 
        elif self.user_input==self.computer:       
            print("Die Game!!!")
        else:
            print("Computer win!!!") 

while True:
    # main program
    message ="""
    1. Scissors
    2. Paper
    3. Rock
    4. Exit
    """

    user_input =input(message)
    if user_input=='1':
        user_input='scissors'
    elif user_input=='2':
        user_input='paper'
    elif user_input=='3':
        user_input='rock'
    elif user_input=='4':
        exit()
    else:
        print("Invalid option!!!")
        
        

    t =Tiktak(user_input)
    t.game()


    
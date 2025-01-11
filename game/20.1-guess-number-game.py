#WAP to perform guess number game
import random

count =0
random_number = random.randint(1, 100)
system=True

while system:
    print("Enter the Number to guess")
    user_guess =int(input())

    if random_number<user_guess:
        print("Guess is Higher,Enter lower Number")
        count=count+1
    elif random_number>user_guess:
        print("Guess is Lower,Enter Higher Number")
        count=count+1
    else:  
        print(f"Congratulation Your Guess Is Correct,attempt times {count}")
        system=False  
    
    


    
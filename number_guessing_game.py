#number guessing game 
#program consist of 
#1. Generating arandom number 
#2. Taking input from the user 
#3. Provinding hints 
#4. Tracking attempts 

import random

while True:
    #generate a random number 
    number_to_guess = random.randint(1,50)
    attempts = 0

    print("\nWelcome tot the number guess game!")
    print("\nI have Choosen a number between 1 t0 50. can you guess it?")

    while True:
        try:
            #take input from the user
            user_guess = int(input("Enter your guess between (1 to 50)"))
            attempts+=1

            #provide hints 
            if user_guess < number_to_guess:
                print("Too low! try again")
            elif user_guess > number_to_guess:
                print("Too high! try again")
            else:
                print(f"Congratualtions! you guessed the number in {attempts} attmepts")
                break
        except ValueError:
            print("Please enter a valid number")

# ask the user if they want to play again
    play_again = input("Do you wnat to play again?(Yes/No)").lower()
    if play_again !='yes':
        print("Thanks for playing! Goodbye")
        break


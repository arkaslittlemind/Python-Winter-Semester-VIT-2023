import random

secretNum = random.randint(1, 100)
noOfGuesses = 5

print("Welcome to the Guessing Game!")
print("You have 5 chances to guess the number between 1 and 100")

while(noOfGuesses):
    guess = int(input("Enter your guess(1-100):"))
    if(guess == secretNum):
        print("Congratulations! You guessed the number!")
        break
    
    elif(guess < secretNum):
        print("HIGHER", noOfGuesses - 1, "guesses left")
        noOfGuesses -= 1
        
    else:
        print("LOWER", noOfGuesses - 1, "guesses left")
        noOfGuesses -= 1
        
if(guess != secretNum):
    print("You have lost the game! The Secret Number was", secretNum)
    
        

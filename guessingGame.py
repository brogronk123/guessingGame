import random

number = random.randint(1,9)
chances = 0
print("Guess a number 1-9")
while chances < 5:
    guess = int(input("What is your guess: "))
    if(guess == number):
        print("Congrats! You win!")
        break
    elif(guess < number):
        print("Your guess was to small: Guess a number bigger then", guess, "you have", 5-chances-1, "guesses left.")
    else:
        print("Your guess was to big: Guess a number smaller then", guess, "you have", 5-chances-1, "guesses left.")
    chances += 1
if not chances < 5:
    print("You lose, the number was: ", number)
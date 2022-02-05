import random
#Heading
print("Number Guessing Game!😊😊😊")

number = int ( random.randint(1,9) )
chance=0
print("Guess a number (between 1 and 9):")
print("You have 5 chances to guess the number...")

while chance < 5:
    guess = int(input("Enter your guess: "))
    chance = chance + 1

    if guess < number:
        print("Your guess was too low! Guess a number higher than ", guess)
        
    if guess > number:
        print("Your guess was too high! Guess a number lower than ", guess)

    if guess == number:
        print("You win!!!")
        print("Hurrayyyyy 🥳🥳🥳")
        break

    if not chance < 5:
        print("You lose! The number is ", number)
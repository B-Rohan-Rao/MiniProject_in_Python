import random


def play():
    number = random.randint(1, 100)

    def lives():
        level = input("Enter the level of game('e' for easy and 'h' for hard): ")
        if level == 'e':
            life = 10
            print("You have 10 lives")
        elif level == 'h':
            life = 5
            print("You have 5 lives")
        else:
            print("Invalid input")
            return lives()  # Ask again if input is invalid
        return life

    life = lives()  # Update the life variable with the returned value

    print(number)  # For debugging, remove this in the actual game
    print(f"You have {life} lives left")
    guess = int(input("Guess a number:\n"))

    while life > 0 and guess != number:
        if guess < number:
            print("Too low!")
            life -= 1
        elif guess > number:
            print("Too high!")
            life -= 1
        print(f"You have {life} lives left")
        if life > 0:
            guess = int(input("Guess a number:\n"))

    if guess == number:
        print("You won!")
    else:
        print("You ran out of lives")


play()

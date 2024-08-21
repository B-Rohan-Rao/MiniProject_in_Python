import random


def random_cards():
    """Reruns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and returns the total score. It also takes care of the ACE"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user, computer):
    """Used to compare the scores"""
    if user == computer:
        return "It is a draw"
    elif computer == 0:
        return "You lose, Computer has a BlackJack"
    elif user == 0:
        return "You win, You have a BlackJack"
    elif user > 21:
        return "You loose, You went over"
    elif computer > 21:
        return "You win, Computer went over"
    elif user > computer:
        return "You win"
    else:
        return "You loose"


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(random_cards())
    computer_cards.append(random_cards())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards {user_cards}, and your score is {user_score}")
        print(f"computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type Y for another car and N for pass:\n").lower()
            if user_should_deal == "y":
                user_cards.append(random_cards())
            elif user_should_deal == "n":
                is_game_over = True
            else:
                print("Invalid input")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards {user_cards}, and your score is {user_score}")
    print(f"computer's first card is {computer_cards}, and computer score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of Black jack(Type 'y' or 'n'):\n") == "y":
    print("\n"*30)
    play_game()

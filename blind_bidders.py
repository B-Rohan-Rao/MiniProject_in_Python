bids = {}
bidding_finished = False


def find_highest_bidders(bidders_record):
    highest_bid = 0
    winner = ""
    for bidder in bidders_record:
        bid_amount = bidders_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# More refined and shorter Version of the above function can be written as below -->
"""
def find_highest_bidders(bidders_record):
    winner = max(bidders_record, key=bidders_record.get)
    highest_bid = bidders_record[winner]
    print(f"The winner is {winner} with a bid of ${highest_bid}")
"""

while not bidding_finished:
    name = input("Enter your name \n")
    price = int(input("What is your bid? \n"))
    bids[name] = price
    should_continue = input("Are there more bidders (Type 'y' or 'n')? \n")
    if should_continue == "n":
        find_highest_bidders(bids)
        bidding_finished = True
    elif should_continue == "y":
        print("\n" * 100)
    else:
        print("Not valid")
        find_highest_bidders(bids)
        bidding_finished = True
        

"""
Explanation for the refined function.
-max() function: The max() function is used to find the key (bidder's name) with the highest value (bid amount) in the 
bidders_record dictionary.
-key=bidders_record.get tells max() to compare the dictionary values (bids) rather than the keys (bidder names).
-winner: The winner variable stores the name of the bidder with the highest bid.
-highest_bid: The highest_bid is then obtained by accessing the dictionary with the winner key.
"""

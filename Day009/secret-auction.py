import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
print(logo)

bids = {}
bidding_end = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_end:
    name = input("What's your name? ")
    price = int(input("How much you bid for? $"))

    bids[name] = price

    should_continue = input("Any more bidders? 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_end = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()




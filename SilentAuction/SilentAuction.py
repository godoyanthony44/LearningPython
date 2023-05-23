print("Welcome to the Silent Auction house")

bidding = True;
bidders ={}
while(bidding):
    name = input("What is your name? ")
    bid = input("What is your bid amount? ")
    bidders.update({name:bid})
    still_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if still_bidders == 'no':
        bidding = False

winner = max(bidders, key=bidders.get)
winner_bid = max(bidders.values())



print(f"The winner is {winner} with the bid of $ {winner_bid}")
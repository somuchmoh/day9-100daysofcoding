from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the silent auction program.")

#empty variables
bidding_list = { }
highest_bid = 0

#function for bidding
def bid(name, bid_amt):
    bidding_list[name] = bid_amt

go_again = True
while go_again == True:
    name = input("What is your name? \n")
    bid_amt = int(input("What's your bid? \n $"))
    bid(name, bid_amt)

    restart = input("Is there another bid? Type 'yes' or 'no'\n")
    if restart == 'no':
        go_again = False
        for name in bidding_list:
            if bidding_list[name] > highest_bid:
                highest_bid = bidding_list[name]
                bidder_name = name
        print(f"{bidder_name} has the highest bid of ${highest_bid}")
    else:
        go_again = True
        clear()

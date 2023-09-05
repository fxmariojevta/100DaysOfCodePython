from art import logo

def highestBid(actionUser):
    bider = ""
    highest = 0

    for key, value in actionUser.items():
        if value > highest:
            highest = value
            bider = key
    
    return bider, highest

if __name__ == "__main__":
    auctionUser = dict()

    print(logo)
    print("Welcome to the secret auction program.")
    while True:
        name = input("What is your name?: ")
        if name in auctionUser:
            print("Name already registered. Please input different name!")
            continue

        bid = int(input("What's your bid?: $"))

        auctionUser[name] = bid

        loop = input("Are there any other bidders? Type 'yes' or 'no'. ")
        if loop == "no":
            break

    winnerBid, bidHighest = highestBid(auctionUser)

    print(f"The winner is {winnerBid} with a bid of ${bidHighest}")
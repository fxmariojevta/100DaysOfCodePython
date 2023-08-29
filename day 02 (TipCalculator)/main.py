if __name__ == '_main_':
    print("Welcome to the tip calculator.")
    total = float(input("What was the total bill? $"))
    percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    tip = total * percentage / 100
    bill = total + tip
    result = bill / people

    print(f"${result:.2f}")
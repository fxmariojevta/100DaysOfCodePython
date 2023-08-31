import random

if __name__ == "__main__":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    nPassword = nr_letters + nr_symbols + nr_numbers
    passwordArray = []
    passwordOrderArray = []

    # this loop can be change into function
    for i in range(0, nPassword):
        passwordArray.append(i)
        passwordOrderArray.append(i)

    for _ in range(0, nr_letters):
        randOrder = random.choice(passwordOrderArray)
        randLetters = random.choice(letters)
        passwordArray[randOrder] = randLetters
        passwordOrderArray.remove(randOrder)

    for _ in range(0, nr_symbols):
        randOrder = random.choice(passwordOrderArray)
        randSymbols = random.choice(symbols)
        passwordArray[randOrder] = randSymbols
        passwordOrderArray.remove(randOrder)

    for _ in range(0, nr_numbers):
        randOrder = random.choice(passwordOrderArray)
        randNumber = random.choice(numbers)
        passwordArray[randOrder] = randNumber
        passwordOrderArray.remove(randOrder)

    print(("").join(passwordArray))
from art import logo

def chiper(text, shift):
    output = ""
    nAlphabet = len(alphabet)

    if not text.isalpha():
        print("Invalid character in text!")
        return
    
    for c in text:
        i = alphabet.index(c)
        iShift = (i + shift) % nAlphabet
        output += alphabet[iShift]

    return output

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = ""
    if direction.lower() == "encode":
        result = chiper(text=text, shift=shift)
    else:
        result = chiper(text=text, shift=-shift)
    
    print(f"Here's the {direction}d result: {result}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye!")
        break
import random
from hangman_art import stages, logo
from hangman_words import word_list

if __name__ == "__main__":
    print(logo)
    life = len(stages) - 1

    wordChoice = random.choice(word_list)
    wordLength = len(wordChoice)
    print(f'Pssst, the solution is {wordChoice}.')

    answer = ["_"] * wordLength

    while "_" in answer:
        letterInput = input("Guess a letter: ").lower()
        if letterInput in answer:
            print(f"You've already guessed {letterInput}")
            continue

        for i in range(wordLength):
            if wordChoice[i] == letterInput:
                answer[i] = letterInput
                continue
        
        print(f"{answer}\n")

        if letterInput not in answer:
            print(f"You guessed {letterInput}, that's not in the word. You lose a life.")
            print(stages[life])
            life -= 1
            if life < 0:
                print("Game Over!")
                break

            continue
            

    if life > 0:
        print("You win!")
    else:
        print("You lose!")
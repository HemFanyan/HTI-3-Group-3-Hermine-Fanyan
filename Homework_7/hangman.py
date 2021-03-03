import random

with open(‘fruits.txt’) as f:
    fruits = [row for row in f.readlines()]
    r_word = random.choice(fruits).strip()


def game(word):
    word = word.upper()

    mistakes = 0
    guessed = set()
    letters = set(word)

    while mistakes < 5:
        print(f"Guess the word. {5 - mistakes} mistakes left.")

        for letter in word:
            if letter in guessed:
                print(f' {letter} ', end='')
            else:
                print(' _ ', end='')

        print()

        guess = input("Guess a letter: ").upper()
        guessed.add(guess)

        if guess not in word:
            mistakes += 1

        if guessed.issuperset(letters):
            for letter in word:
                print(f' {letter} ', end='')

            print()
            print("You won the game.")
            break

    if not guessed.issuperset(letters):
        print("You lost the game.")


game(r_word)


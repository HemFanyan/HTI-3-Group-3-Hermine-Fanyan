def game():
    while True:
        action = input('Think of a number between 1 and 999. Input 0 once you’re ready to play.')
        if action == 0:
            break

    s = 0
    guessed = False
    start = 1
    end = 999

    while s < 10:
        s = s + 1
        guess = (start + end) // 2
        print(f'My guess number {s}: {guess}')

        number = input()

        if number == '0':
            print(f'I guessed in {s} steps!')
            guessed = True
            break
        elif number == '-1':
            end = guess - 1
        elif number == '1':
            start = guess + 1
        else:
            print('Invalid number.')
            s = s - 1

    if not guessed:
        print("I couldn’t guess in 10 steps! This means you cheated!")


game()
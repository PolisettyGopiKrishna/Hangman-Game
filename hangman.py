import random

def choose_word():
    words = ["cat", "dog", "ant", "cow", "fun"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts += 1
                print(f"Incorrect guess. {max_attempts - attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()

import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "software"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()

    # Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Incorrect guesses left:", max_attempts - incorrect_guesses)

# If the player uses all attempts
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")
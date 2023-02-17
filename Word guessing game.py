import random

# List of words to choose from
words = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the unknown word
word_display = ['_' for letter in word]

# Number of guesses the player has
guesses = 6

# Keep track of guessed letters
guessed_letters = []

# Game loop
while True:
    # Print the current state of the word
    print(' '.join(word_display))

    # Get a guess from the player
    guess = input('Guess a letter: ')

    # Check if the guess has already been made
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print('Correct!')

        # Update the word display with the guessed letter(s)
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        print('Incorrect.')
        guesses -= 1

    # Check if the player has won
    if '_' not in word_display:
        print('You win!')
        break

    # Check if the player has run out of guesses
    if guesses == 0:
        print('You lose! The word was', word)
        break

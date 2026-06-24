# Hangman Project To-Do List
# 1. Set up the game
import random

words = ["lantern", "biscuit", "orbit", "velvet", "canyon", "whisper", "marble", "tornado", "paperclip", "nebula", "cinnamon", "glacier", "riddle", "flame", "echo", "pocket", "harbor", "comet", "drift", "mosaic", "thunder", "plum", "vortex", "linen"]

randomWord = random.choice(words)
length_word = len(randomWord)

print(randomWord)

correctWord = []

# 2. Prepare game variables

remainingGuesses = 12

guessed_letters = set()

all_letters = ""

# 3. Display the hidden word
display = ""

for n in range(length_word):
 display += "_"

print(display)


for letters in randomWord:
 display = "_"
 correctWord.append(display)

print("".join(correctWord))

#  Show underscores (_) for unguessed letters.



#  Reveal letters that have been guessed correctly.
# 4. Get player input
#  Ask the player to enter a letter.
#  Validate the input:
#  Ensure only one character is entered.
#  Ensure it is a letter.
#  Check if it has already been guessed.
# 5. Process guesses
#  If the letter is in the word:
#  Add it to the correct guesses.
#  Update the displayed word.
#  If the letter is not in the word:
#  Decrease the remaining guesses.
#  Inform the player.
# 6. Add Hangman visuals (optional)
#  Create ASCII-art stages of the hangman.
#  Display the correct stage based on remaining guesses.
# 7. Check for game-ending conditions
#  Win condition:
#  All letters in the word have been guessed.
#  Lose condition:
#  Remaining guesses reach zero.
# 8. End the game
#  Display a win or lose message.
#  Reveal the secret word if the player loses.
# 9. Add replay functionality (optional)
#  Ask the player if they want to play again.
#  Restart the game if they choose "yes".
# 10. Test and improve
#  Test with different words.
#  Test invalid inputs.
#  Fix bugs and improve messages.
#  Add features such as difficulty levels, hints, or scoring.
# Recommended build order
# Random word selection
# Display underscores
# Letter input
# Correct/incorrect guess handling
# Win/lose detection
# Hangman ASCII art
# Replay option
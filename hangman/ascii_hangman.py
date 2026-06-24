import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#taking one word by hazard and saving it in a variable
random.choice(words)

the_correct_word = random.choice(words)

#splitting the letters of the chosen word in single characters

split_letters = list(enumerate(the_correct_word))


# We define the variables for the number of mistakes
# and create an empty list to later save the length of
# the word and his correctly guessed letters


mistakes = 0
show_letters = []
normal_seen_letters = ""

# we create the underscores for the correct word

for letter in split_letters:
    show_letters += "_"

# the game keeps going until the hangman is full hence to many mistakes were done

while mistakes < len(HANGMANPICS) - 1:

# here we print each underscore standing for a letter of the word

    for l in show_letters:
        normal_seen_letters = "".join(show_letters)

    print(normal_seen_letters)

# we ask the user to give an input

    guessed_letters = input("guess the word, write a letter or write the word: ")

# here we compare all the letters in the correct word to match them
# with the guessed input of the user

    for index, letters in enumerate(the_correct_word):

        if guessed_letters == letters:

            show_letters[index] = guessed_letters

# If they are not in the correct word a mistake gets added and a pic of hangman is printed

    if guessed_letters not in the_correct_word:
        mistakes += 1
        print(HANGMANPICS[mistakes])

# finally we compare if the mistakes are too high the game is over, or if the user manages
# to get right the word the game is won

    if mistakes == len(HANGMANPICS) - 1:

        print(f"game over, the correct word was {the_correct_word}")

    if guessed_letters == the_correct_word:
        mistakes = 10
        print(f"you won, {guessed_letters} is correct")
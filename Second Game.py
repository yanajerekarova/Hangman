import random


def load_words(filename):
	#with open(filename, 'r') as f:
	#	file_string = f.read()
	#words = file_string.split()
	words = ['hello', 'bye', 'world']
	return words

def choose_secret_word(words):
	word = random.choice(words)
	return word

def is_secret_guessed(secret_word, letters_guessed):
    all_guessed = True
    for letter in secret_word:
        if letter in letters_guessed:
            all_guessed = True
        else:
            all_guessed = False
            break
    return all_guessed


def get_current_guess(secret_word, letters_guessed):
    result = ''
    for char in secret_word:
        if char in letters_guessed:
            result+=char
        else:
            result+='_'
    return result


def second_game(secret_word):
    secret_word = secret_word.lower()
    num_guesses = 15
    letters_guessed = [] 
    while not(is_secret_guessed(secret_word, letters_guessed)) and num_guesses!=0:
        char = input("Guess a letter: ").lower()
        if len(char) != 1:
            print("Enter one letter only!")
            continue
        letters_guessed.append(char)
        if is_secret_guessed(secret_word, letters_guessed):
            print("You won! :)")
            return 'win'
        if char not in secret_word:
            num_guesses-=1
        print("You have " + str(num_guesses) + " guesses remaining!")
        print(get_current_guess(secret_word, letters_guessed))
    print("You lost! :(")
    return 'lose'

filename = 'words.txt'
words = load_words(filename)
word = choose_secret_word(words)

second_game(word)

def is_secret_guessed(secret_word, letters_guessed):
    """
    Inputs:
    - secret_word (str/list)
    - letters_guessed (str/list)
    Output:
    - all_guessed (bool)
    Description:
    - If all the characters in secret_word are in letters_guessed
    - Returns True
    - Otherwise, returns False
    """
    all_guessed == True
    for letter in secret_word:
        if letter in letters_guessed:
            all_guessed == True
        else:
            all_guessed == False
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


def first_game(secret_word):
    num_guesses = 15
    letters_guessed = [] 
    while not(is_secret_guessed) and guesses!=0:
        char = input("Guess a letter: ").lower()
        if len(char) != 1:
            print("Enter one letter only!")
            continue
        chars_guessed.append(char)
        if is_secret_guessed(secret_word, letters_guessed):
            print("You won! :)")
            break
        if char not in secret_word:
            num_guesses-=1
        print("You have " + str(num_guesses) + " guesses remaining!")
        print(get_current_guess(secret_word, letters_guessed))
    if num_guesses == 0:
        print("You lost! :(")

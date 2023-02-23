# User starts the game from the command line
# A secret word is selected
# User is prompted to guess a letter
# The game checks the letter to see if it is in the word
# The game prints out a section of the snowman drawing, showing one level for each incorrectly guessed letters
# The game prints out a hidden version of the word, where each correct letter is displayed and un-guessed letters are hidden
# The game prints out all of the incorrect letters that have been guessed
# The game loops back to asking the user to guess a letter and continues that pattern until either the user has guessed all of the letters in the word, or the snowman drawing is complete.
# import random
from wonderwords import RandomWord
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5 
SNOWMAN_WRONG_GUESSES = 7
def print_snowman(wrong_guesses_list):
   SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------'
    ] 
   for i in range(SNOWMAN_WRONG_GUESSES - len(wrong_guesses_list),
                SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def get_letter_from_user(word_dict, wrong_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in wrong_guesses_list:
            print("You have already guessed that letter!")
        elif user_input_string in word_dict and word_dict[user_input_string]:
            print("You have already guessed that letter")
        else:
            valid_input = True
    return user_input_string
def build_word_dict(word):
    word_dict = {}
    for letter in word:
        word_dict[letter] = False
    return word_dict
def snowman():
    r = RandomWord()
    snowman_word = r.word(
    word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
    word_max_length=SNOWMAN_MAX_WORD_LENGTH)
    wrong_guesses_list = []
    snowman_dict = build_word_dict(snowman_word)
   
    print(snowman_word)
    
    while len(wrong_guesses_list)< SNOWMAN_WRONG_GUESSES and not get_word_progress(snowman_word, snowman_dict):
        user_input = get_letter_from_user(snowman_dict,wrong_guesses_list)
        if user_input in snowman_dict: 
            print("You guessed a letter that's in the word!")
            
            snowman_dict[user_input] = True
            
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
        print(generate_word_progress_string(snowman_word, snowman_dict))
        print_snowman(wrong_guesses_list)
        print(f"Wrong guesses: {wrong_guesses_list}")
        if get_word_progress(snowman_word, snowman_dict):
            print("YOU WON THE GAME!")
        


            
def generate_word_progress_string(word, word_dict):
    word_progress = ""
    key_num = 0
    for key in word:
        if key_num > 0:
            word_progress += " "
            
            
        if word_dict[key]:
            word_progress += key
            
        else:
            word_progress += "_"
        key_num += 1
    return word_progress
def get_word_progress(word, word_dict):
    Flag = True
    for elem in word:
        if not word_dict[elem]:
            Flag = False
    return Flag


play = snowman()
print(play)
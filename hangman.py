# This program uses the random module and regular expressions module to 
#create a hangman game. Users try to guess a random word picked from a word file

import random # import the random module 
import re # import re module for regular expressions

def display_word(word, guessed_letters):
    display = " " # creates an emptry string to display the word with which letters are to be guessed 
    for letter in word: # checks each letter in the chosen word 
        if letter in guessed_letters:
            display += letter + " " # if guess is correct, add the letter to the display
        else:
            display += "_ "# underscore used as placeholder in the display 
    return display

def get_random_word(file_path):
    with open(file_path, 'r') as file: # open file containing words 
        words = file.read().split() # read words from the file and splits them into a list 
        
        # Filter words to contain only alphabetic characters  (no words with special characters )
        words = [word.lower() for word in words if word.isalpha()]
        return random.choice(words) # returns a random word from the filtered word list 

def main(): # function for main game 
    file_path = r'C:\Users\donko\INST\word_search\text1_folder\pet_shoppe.txt' #filepath to get word from
    chosen_word = get_random_word(file_path) # gets a random word from the file 
    guessed_letters = [] # varibale to store the guessed letters in a list 
    attempts = 7
    
    print("Lets play Hangman!")
    print(display_word(chosen_word, guessed_letters))
    
    # loops until attempts run out
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
    # checks if the guess uses a single letter with regular expressions
        if not re.match("^[a-zA-Z]$", guess):
            print("Please enter a single letter.")
            continue
    
    # checks if letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess) # adds the guessed letter to the list 
        
        if guess not in chosen_word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        word_display = display_word(chosen_word, guessed_letters) # updates the displayed word with correct guesses
        print(word_display)
    
    # checks to see if all the letters have been guessed 
        if '_' not in word_display:
            print("Congratulations! You guessed the word!")
            break
    
    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{chosen_word}'")

main() # Starts game 

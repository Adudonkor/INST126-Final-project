import random # import random module to get random number 
import pandas as pd # import panda library to organize Dataframes

def guess_number(): # function for whole code 
    
    number = random.randint(1, 100) # Generate a random number between 1 and 100
    
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Reads existing game data from CSV file 
    try: # checks to see if file exists 
        game_data = pd.read_csv('game_results.csv')
    except FileNotFoundError:
        
        # create an empty DataFrame if file doesn't exist
        game_data = pd.DataFrame({'Secret_Number': [], 'Attempts': [], 'Outcome': []})



    while attempts < max_attempts: # starts the game loop with limited number of attempts 
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        

        # checks if the guess is too high or lower or equal to secret number
        if guess < number:
            print("Too low! Try guessing a higher number.")
        elif guess > number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You've guessed the number ({number}) in {attempts + 1} attempts!")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number I was thinking of was {number}.")
        
    # Creates a dictionary with the new game result
    new_result = {'Secret_Number': number, 'Attempts': attempts + 1,}
    
    # Converts the new game result to a DataFrame and adds it to the existing data
    new_data = pd.DataFrame([new_result])
     # combines the new_data with the already exisitng game data
    game_data = pd.concat([game_data, new_data], ignore_index=True)
    
    # Creates a new coloum in the DataFrame called "Outcome", checks the value of "Secret number" 
    # and returns success or failure depenidng on whether the secret number was correctly guessed that round
    # lambda is essentailly used as an unnamed function here  
    game_data['Outcome'] = game_data['Secret_Number'].apply(lambda x: 'Success' if x == number else 'Failure')
    
    # Get a subset of the DataFrame using a boolean condition to fulfil 8.3
    successful_attempts = game_data[game_data['Outcome'] == 'Success']
    
    # loads new data to the CSV file
    game_data.to_csv('game_results.csv', index=False)

# Run the game
guess_number()

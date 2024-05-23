import random
from typing import List, Callable

# Function that reads words file and returns a list
def create_word_list(word_file: str) -> List[str]:
    with open(word_file, 'r') as file:
        return [line.strip() for line in file]

# Lambda function to select a random word from the list
select_word_solution: Callable[[List[str]], str] = lambda words: random.choice(words)

# Lambda function that compares the guessed word to the target word:
# - The actual letter if it's correct and in the correct position
# - '[The guessed letter]' if the letter is in the target word but in the wrong position
# - '_' if the letter is not in the target word
check_attempt: Callable[[str, str], List[str]] = lambda word_solution, guess: [
    (word_solution[i] + ' ') if word_solution[i] == guess[i] 
    else ('[' + guess[i] + '] ') if guess[i] in word_solution 
    else '_ '
    for i in range(len(word_solution))
]

# Recursive function to play each attempt
def play_attempt(word_solution: str, words: List[str], attempts: int) -> Callable[[], str]:
    def attempt_function() -> str:
        if attempts == 0:
            return f"Game Over! The word was: {word_solution}"
        
        guess = input("Enter your guess: ").strip().lower()
        
        # Validate the guess
        if guess not in words:
            print("Invalid word. Try again.")
            return play_attempt(word_solution, words, attempts)()  # Recursively call for the same attempt
        
        feedback = check_attempt(word_solution, guess)
        
        print(''.join(feedback))
        if guess == word_solution:
            return "Correct! You've guessed the word!"
        
        return play_attempt(word_solution, words, attempts - 1)()  # Recursively call for the next attempt
    
    return attempt_function

# Main game function to initialize and start the game
def wordle_game(word_file: str, attempts: int = 6) -> None:
    words = create_word_list(word_file)  # Load words from the file
    word_solution = select_word_solution(words)  # Select a random target word
    result = play_attempt(word_solution, words, attempts)()  # Start the game
    print(result)

# Start the game
wordle_game('words.txt')

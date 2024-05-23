# Wordle using Functional Programming


## Description


**Problem to solve using a programming paradigm:**  
Wordle is a popular word-guessing game where players need to guess a five-letter word within six attempts. After each guess, players receive feedback in the form of colored tiles indicating correct letters in the correct position (green), correct letters in the wrong position (yellow), and incorrect letters (grey). The goal is to guess the target word using the given feedback.


The paradigm that will be used as a base to solve the problem is **functional programming**, which integrates lambda calculus into programming. This significantly changes the paradigm because we no longer have states but functions, making it easier to use recursion rather than iterations. Lambda calculus (λ-calculus) is a mathematical system for expressing computation based on function abstraction and application, associating variables with functions with their arguments and using variable substitution (Chowdhary, 2021).


**Key features of functional programming include:**


- **Immutability:** Once data is created, it does not change state.  
  *Wordle uses many words to choose from, during the game they should not be altered. Since previous states are not altered, it reduces bugs related to state changes.*


- **Pure Functions:** Functions have no side effects and return the same output for the same input.  
  *Given the same guess, the feedback and resulting state is always the same.*


- **First-Class Functions:** Functions are treated as first-class citizens, meaning they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.


- **Higher-Order Functions:** Functions can take other functions as arguments or return them as results.


- **Declarative Style:** Focuses on what to solve rather than how to solve it, emphasizing expressions and declarations over statements and commands.


## Models


**Logic of the solution and how the paradigm would be used:**


**Functional programming in the code:**


- **Immutability:** Once data is created, it does not change state.  
  *Can be seen in the words list and `word_solution` not being altered during the game's execution. The game state is maintained by passing updated attempts and feedback without modifying the original inputs.*


- **Pure Functions:** Given the same guess, the feedback and resulting state is always the same.  
  *The `check_attempt` function is pure. It takes the word solution and current guess as inputs and returns feedback without causing side effects or relying on external state.*


- **First-Class Functions:** Functions are assigned to variables, passed as arguments, returned from other functions.  
  *Functions `check_attempt` and `play_attempt` are treated as first-class citizens. They are passed around as arguments and returned as values. The `play_attempt` function returns the `attempt_function` function, showcasing the ability to return functions from other functions.*


- **Higher-Order Functions:**  
  *`play_attempt` returns a function that performs the game round logic. This encapsulates the game state within the function and maintains immutability. `select_word_solution` is a lambda function that selects a target word from the list, demonstrating the use of first-class and higher-order functions.*


- **Declarative Style:**  
  *The game logic focuses on generating feedback and validating guesses rather than how to manage the state transitions explicitly. The recursive approach in `play_attempt` handles the game flow declaratively. Although we do have a number of attempts for the specifications of the game, we focus on recursion rather than iteration. The `play_attempt` function is defined recursively to play each attempt, rather than using a loop structure.*


## Implementation


The implementation of the solution was done in Python. Although it is not exclusively a functional programming language, it does support the paradigm, incorporating several features that facilitate it. 


**For the implementation the feedback is given in the following way:**


- Correct letters in the correct position (The actual letter is returned)
- Correct letters in the wrong position ('[ The guessed letter ]')
- Incorrect letters ('_')


Have in mind that the file “words.txt” must also be in the folder. The words you submit as guesses must be in this file to be valid. 
**Example:**  
For the following target word: exalt


- Guess: audio  
  Feedback: [a] _ _ _ _


- Guess: house  
  Feedback: _ _ _ _ [e]


- Guess: exalt  
  Feedback: exalt


> [!TIP]
>
> **To test it in a terminal in Windows:**
1. Navigate to the directory where `wordle.py` is located.
2. Run the script by typing `python wordle.py`.
3. Enter your attempts to guess the word.
> 
**To test it in a terminal in Windows:**


1. Navigate to the directory where `wordle.py` is located.
2. Run the script by typing `python wordle.py`.
3. Enter your attempts to guess the word.


## Tests


*Add tests and how to run them.*


## Analysis


**Possible paradigms that can be used to solve the problem**
Logic Programming:  
Logic programming is a paradigm based on defining facts rules and relationships. 

For Wordle:
- Define the dictionary of words as facts.
- Define the rules for guessing and feedback.

**Time complexity of my solution**

`create_word_list`: O(n) where n is the number of words
`select_word_solution`: O(1)
`check_attempt`: O(m) where m is the length of the word

`play_attempt`: O(n+m), where n is the number of words in the list and m is the length of the word.
Since this function can be called up to attempts times, the worst-case time complexity is O(attempts×(n+m)).

The overall Time Complexity is O(attempts×(n+m)), where attempts is 6 so time complexity can be deduced as O(n).


## References


Chowdhary, K. (2021). Theory of Formal Languages (Introduction to Lambda-calculus). Retrieved from: [https://krchowdhary.com/tfl/tfl-l16.pdf](https://krchowdhary.com/tfl/tfl-l16.pdf)



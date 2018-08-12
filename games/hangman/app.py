import random

words_set = {'family','food','software','science','	language','	night'}

word = random.choice(list(words_set))
solved = [None] * len(word)
wrong_guesses = []


stage_repr = [
'''
 +---+
     | 
     | 
     | 
    ===
''',
'''
 +---+
 O   | 
     | 
     | 
    ===
''',
'''
 +---+
 O   | 
 |   | 
     | 
    ===
''',
'''
 +---+
 O   | 
/|   | 
     | 
    ===
''',
'''
 +---+
 O   | 
/|\  | 
     | 
    ===
''',
'''
 +---+
 O   | 
/|\  | 
/    | 
    ===
''',
'''
 +---+
 O   | 
/|\  | 
/ \  | 
    ===
''',
]


def get_solved_str():
    return ' '.join([c if c else '_' for c in solved])


def get_wrong_guesses_str():
    return ', '.join(wrong_guesses)


def apply_guess(guess):
    if guess in word:
        for k, c in enumerate(word):
            if c == guess:
                solved[k] = guess
    else:
        wrong_guesses.append(guess)


def is_won():
    return None not in solved

def is_lose():
    return len(wrong_guesses) == len(stage_repr) - 1

while True:
    print('-'*30)
    print('solved word:', get_solved_str())
    print('wrong guesses:', get_wrong_guesses_str())
    print( stage_repr[len(wrong_guesses)])

    if is_lose():
        print('Game over. You lose')
        break
    elif is_won():
        print('You win')
        break
    
    guess = input('Guess a letter: ')

    if guess in wrong_guesses or guess in solved:
        print('You already guessed this letter')
        continue
    
    apply_guess(guess)


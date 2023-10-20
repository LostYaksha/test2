import random


def reveal_world(guess, random_word, word):
    return ''.join([rand_word[i] if rand_word[i].upper() == guess.upper() else word[i] for i in range(len(rand_word))])


with open('sowpods.txt', 'r') as f:
    lines = f.read().split()
rand_word = random.choice(lines)
print(rand_word)
word = rand_word[0] + '*' * (len(rand_word) - 2) + rand_word[-1]
print('welcome tho the game. ')
print(word)
while '*' in word:
    guess = input('Guess a letter: ')
    if guess.upper() in rand_word:
        print('Correct')
        word = reveal_world(guess, rand_word, word)
        print(word)
    else:
        print('Wrong')

print('Congratulations! You have completed the word!')


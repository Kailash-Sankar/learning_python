# program to play hangman
import random


# get random word
def get_word():
    fin = open('words.txt', 'r')
    words = fin.readlines()
    fin.close()
    return random.choice(words)


def get_indexes(a, e):
    wordlist = list(a)
    indexes = []
    for i in range(0, len(wordlist)):
        if e == wordlist[i]:
            indexes.append(i)
    return indexes


# main
word, hint = get_word().strip().split('#')
guessword = list('-' * len(word))
lives = 7

#print word, guessword, hint

# loop
print 'Guess this famous game'
print 'Hint:', hint

while True:
    print guessword
    print 'Lives left:',lives
    guess = raw_input('Enter character to guess')
    guess =  guess.lower()
    indexes = get_indexes(word, guess)
    if indexes:
        for i in indexes:
            guessword[i] = guess

        if guessword == list(word):
            print word
            print 'You won the game'
            break;
    else:
        lives = lives - 1

    if lives == 0:
        print 'Game Over!!'
        break;

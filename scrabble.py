#!/usr/bin/env python

#kristenwidman
#May 2, 2013

#problem description: 
#  Given 7 letters, return the sorted list of words you can make
#   including blanks

#brute force:
# pick one letter, check if in dictionary
# check all 1 letter combos, then all 2 letter, up to all 7

import sys
from string import lower
from itertools import permutations

def check_if_word(word):
    '''Checks the list of words (dictionary) for occurence of the word.
        Input words are converted to lowercase and compared to the dictionary.
        Uppercase words in the dictionary are ignored because Scrabble
        does not allow proper nouns.
    '''
    dictionary = open('/usr/share/dict/words', 'r')
    word = '\n'+lower(word)+'\n' #find only this word, not as a substring in another word
    if word in dictionary.read():
        return True
    else: return False

def create_permutations(letters, n, word=''):
    '''an alternative to itertools.permutations(). practice with recursion
        and generators'''
    if n == 0:
        yield word
    else:
        for i in range(len(letters)):
            for perm in create_permutations(letters[:i] + letters[i+1:], n-1, word+letters[i]):
                yield perm

def all_n_perms(word, n):
    '''Itertools.permutations() and create_permutations() both create permutations
        of a specified length. This function calls these as submethods for all
        lengths less than or equal to n.
    '''
    for i in range(1,n+1):
        for p in permutations(word, i):
        #for p in create_permutations(word, i):
            yield p

def main(word, n):
    for word in all_n_perms(word, n):
        word = ''.join(word) #only include this line when using itertools fct
        if check_if_word(word):
            print word

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

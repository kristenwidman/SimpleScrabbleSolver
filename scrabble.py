#!/usr/bin/env python

#kristenwidman
#May 2, 2013

#problem description:
#  Given 7 letters, return the sorted list of words you can make
#   including blanks

import sys
from string import lower, lowercase
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

def handle_blanks(word, n):
    '''Method to handle dealing with blanks, represented by '_'.
        Removes the blank from the word and replaces it with
        every character, running the main program on each character
        set. Uses sets to hold all matching words to not get
        duplicates.
    '''
    position = word.index('_')
    word = word[:position] + word[position+1:]
    word_set = set([])
    for c in lowercase:
        word_set = run(word+c, n, word_set)
    return word_set

def run(word, n, word_set):
    '''Create all permutations possible for the given letters that are
        shorter than or equal to the specified length. Check each permutation
        to see if it is in the dictionary. If it is, add it to the set.
        Return the set of words.
    '''
    for perm in all_n_perms(word, n):
        perm = ''.join(perm) #only include this line when using itertools fct
        if check_if_word(perm):
            word_set.add(perm)
    return word_set

def main(word, n):
    '''
        Main method.
        Written to use either itertools.permutations() or my own simple
        permutation creation method 'create_permutations()'.
    '''
    if '_' in word:
        word_set = handle_blanks(word, n)
    else:
        word_set = run(word, n, set([]))
    for allowed in word_set:
        print allowed

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

#!/usr/bin/env python

#kristenwidman
#May 6, 2013

#problem description: 
#  Given 7 letters, return the sorted list of words you can make
#   including blanks

import sys
import re
from string import lower, strip

def remove_char(chars, c):
    position = chars.index(c)
    return chars[:position] + chars[position+1:]

def compare_letters(word, chars):
    '''For a given word and set of characters, checks each letter
        in the word to see if it is in the character set. If not,
        returns False. If it is, the character is removed from the
        character set and the comparison continues for the remaining
        characters in the word. If all characters in the word are
        in the char set, returns True.
        Handles blanks, represented by '_' character.
        Uppercase words from the dictionary are considered proper
        nouns and excluded.
    '''
    for c in word:
        if c not in chars:
            if '_' not in chars or c.isupper(): #accounts for blanks. Uppercase words not allowed.
                return False
            else:
                chars = remove_char(chars, '_')
        else:
            chars = remove_char(chars, c)
    return True

def main(chars, n):
#alternate way:
#compare every word in dictionary to list of characters you have.
# any words that have any characters you do not have, remove from
# dictionary list.
    '''Compares every word in the dictionary to a string of characters.
        Discards words that are too long or have characters not in the
        allowed char set.
    '''
    dictionary = open('/usr/share/dict/words','r')
    for word in dictionary:
        word = word.strip()
        if len(word) <= n:  #don't do char comparison if the word is too long
            if compare_letters(word, lower(chars.strip())):
                print word

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))


#!/usr/bin/env python

#kristenwidman
#May 6, 2013

#problem description: 
#  Given 7 letters, return the sorted list of words you can make
#   including blanks

#alternate way:
#compare every word in dictionary to list of characters you have.
# any words that have any characters you do not have, remove from
# dictionary list.

import sys
import re
from string import lower, strip

def compare_letters(word, chars):
    for c in word:
        if c not in chars:
            return False
        else:
            position = chars.index(c)
            chars = chars[:position] + chars[position+1:]
    return True

def main(chars, n):
    dictionary = open('/usr/share/dict/words','r')
    for word in dictionary:
        word = word.strip()
        if len(word) <= n:  #don't do char comparison if the word is too long
            if compare_letters(word, lower(chars.strip())):
                print word

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))


#!/usr/local/bin/python3

def make_abbr(word):
    if len(word) < 3:
        return word

    vowels = 'aeiou'

    abbr = -1
    for idx in range(1, len(word)):
        if word[idx] in vowels:
            abbr = idx

    # no vowels, no abbreviation
    if abbr == -1:
        return word
    else:
        return word[0] + str(abbr) + word[-1]
    
def unique_word_abbreviation(lword, word_dict):
    '''
    An abbreviation of a word follows the form 
    <first letter><number><last letter>. Below are some 
    examples of word abbreviations:

    a) it                      --> it    (no abbreviation)

         1
         ↓
    b) d|o|g                   --> d1g

                  1    1  1
         1---5----0----5--8
         ↓   ↓    ↓    ↓  ↓    
    c) i|nternationalizatio|n  --> i18n

                  1
         1---5----0
         ↓   ↓    ↓
    d) l|ocalizatio|n          --> l10n

    Assume you have a dictionary and given a word, find 
    whether its abbreviation is unique in the dictionary. 
    A word's abbreviation is unique if no other word from 
    the dictionary has the same abbreviation.

    Example:

    Given dictionary = [ "deer", "door", "cake", "card" ]

    isUnique("dear") -> false
    isUnique("cart") -> true
    isUnique("cane") -> false
    isUnique("make") -> true

    https://leetcode.com/problems/unique-word-abbreviation/description/
    
    Time :
    Space:
    Note :
    1. abbreviation : <first letter>[last index of vowel]<last letter>
    2. find, create a set of abbreviated
    '''
    
    if lword == None or len(lword) == 0:
        return lword

    abbr_dict = set()
    for word in word_dict:
        abbr_dict.add(make_abbr(word))

    return not (make_abbr(lword) in abbr_dict)

def run():
    '''
    word_dict = [ "deer", "door", "cake", "card" ]
    print(unique_word_abbreviation("dear", word_dict))
    print(unique_word_abbreviation("cart", word_dict))
    print(unique_word_abbreviation("cane", word_dict))
    print(unique_word_abbreviation("make", word_dict))
    '''
    word_dict = [ "hello" ]
    print(unique_word_abbreviation("hello", word_dict))



if __name__ == '__main__':
    run()


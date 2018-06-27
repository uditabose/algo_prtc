
def reverse_vowels_of_a_string(astr):
    '''
    Write a function that takes a string as input and 
    reverse only the vowels of a string.

    Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede".

    Note:
    The vowels does not include the letter "y".

    https://leetcode.com/problems/reverse-vowels-of-a-string/description/

    Time : O(N)
    Space: O(N)
    Note :
    1. 2 indices left and right
    2. progress if index is a consonant
    3. stop and swap if both are vowels, then move both
    4. repeat till left < right
    '''
    if astr == None or len(astr) == 0:
        return astr

    left = 0
    right = len(astr) - 1
    reversed_astr = [''] * len(astr)

    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    while left < right:
        if astr[left] in consonants:
            reversed_astr.insert(left, astr[left])
            left += 1

        if astr[right] in consonants:
            reversed_astr.insert(right, astr[right])
            right -= 1

        if astr[left] in vowels and astr[right] in vowels:
            reversed_astr.insert(right, astr[left])
            reversed_astr.insert(left, astr[right])
            left += 1
            right -= 1

    return "".join(reversed_astr)

def run():
    print(reverse_vowels_of_a_string("hello"))
    # holle
    print(reverse_vowels_of_a_string("leetcode"))
    # leotcede

    '''
    holle
    leotcede
    '''

if __name__ == '__main__':
    run()


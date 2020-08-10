#!/usr/local/bin/python3

def word_ladder(begin_word, end_word, word_list):
    '''
    Given two words (beginWord and endWord), and a dictionary's 
    word list, find the length of shortest transformation sequence 
    from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. 
    Note that beginWord is not a transformed word.
    Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and 
    are not the same.
    Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is 
    "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    Example 2:

    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    Output: 0

    Explanation: The endWord "cog" is not in wordList, 
    therefore no possible transformation.
        
    https://leetcode.com/problems/word-ladder/description/

    Time : O(N)
    Space: O(k)
    Note :
    1. initialize current word to begin word, steps to zero 
    2. start loop
    3. check distance between current word, and loop word
        a. if distance is 1, increment step, loop word to current word
        b. else, move ahead
    4. if loop word is same as end word, would break loop
        a. if distance between word is 1, increment step
        b. else, reset step to zero
    5. return

    > check distance
        1. put current word in a set
        2. put loop word in a set
        3. test difference
            a. if 1, then 3a
            b. else, 3b        

    '''
    if begin_word == None or len(begin_word) == 0:
        return 0
    if end_word == None or len(end_word) == 0:
        return 0
    if word_list == None or len(word_list) == 0:
        return 0
    if end_word not in word_list:
        return 0

    curr_word = begin_word
    steps = 0
    for word in word_list:
        print(len(set(curr_word).difference(set(word))))
        if word == end_word:
            if len(set(curr_word).difference(set(word))) == 1:
                steps += 1
            else:
                steps = 0
            break
        else:
            if len(set(curr_word).difference(set(word))) == 1:
                steps += 1
                curr_word = word

    return steps
        
def run():
    '''
    begin_word, end_word = 'hit', 'cog'
    word_list = ["hot","dot","dog","lot","log","cog"]
    print(word_ladder(begin_word, end_word, word_list))

    begin_word, end_word = 'hit', 'cog'
    word_list = ["hot","dot","dog","lot","log"]
    print(word_ladder(begin_word, end_word, word_list))

    begin_word, end_word = "hit", "hat"
    word_list = ["hot","hat"]
    print(word_ladder(begin_word, end_word, word_list))
    '''

    begin_word, end_word = "hot", "dog"
    word_list = ["hot","dog","dot"]
    print(word_ladder(begin_word, end_word, word_list))
    print("")

if __name__ == '__main__':
    run()


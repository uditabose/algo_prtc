
def reverse_words(astr_list):
    '''
    You're working on a secret team solving coded transmissions.

    Your team is scrambling to decipher a recent message, worried 
    t's a plot to break 
    into a major European National Cake Vault. The message has 
    been mostly deciphered, 
    but all the words are backwards! Your colleagues have handed 
    off the last step to you.

    Write a function reverse_words() that takes a message as a 
    list of characters 
    and reverses the order of the words in-place. ↴

    https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation
    
    Time  : O(N)
    Space : O(1)
    Note  :
    '''
    num_w = astr_list.count(' ')
    astr_list[0:0] = ' '
    popped_w = 0
    w_idx = 0
    count = 0
    while popped_w != num_w:
        last_c = astr_list.pop(-1)
        astr_list[w_idx:w_idx] = last_c 
        if last_c == ' ':
            popped_w += 1
            w_idx = count + 1
        count += 1
    astr_list.pop(0)


if __name__ == '__main__':
    astr_list = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
    print("".join(astr_list))
    reverse_words(astr_list)
    print("".join(astr_list))
    print("")

    astr_list = [ 'c', 'a', 'k', 'e', ' ',
            'd', 'r', 'a', 'm', 'a', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
    print("".join(astr_list))
    reverse_words(astr_list)
    print("".join(astr_list))
    print("")


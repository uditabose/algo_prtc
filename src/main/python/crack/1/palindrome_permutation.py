
def palindrome_permutation(astr):
    '''
    1.4 find if a string a permutation 
                of a palindrome, O(N)
    '''
    astr = astr.lower()
    ch_set = set()
    for c in astr:
        if c == ' ':
            continue
        if c in ch_set:
            ch_set.remove(c)
        else:
            ch_set.add(c)

    return (len(ch_set) == 0 or len(ch_set) == 1)

def run():
    astr = 'Tact Cao'
    print("%s is a palindrome permutation : %r" 
          % (astr, palindrome_permutation(astr)))

if __name__ == '__main__':
    run()


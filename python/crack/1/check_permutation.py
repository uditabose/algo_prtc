
def is_permutation(astr, bstr):
    '''
    1.2 if one is a permutation of other : O(Nlog(N))
    '''
    if len(astr) != len(bstr):
        return False

    astr = sorted(astr)
    bstr = sorted(bstr)

    return (astr == bstr)


def run():
    astr = 'pompop'; bstr = 'dskjhk'
    print("%s is a permutation of %s : %r" 
          % (astr, bstr, is_permutation(astr, bstr)))

    astr = 'lll'; bstr = 'llll'
    print("%s is a permutation of %s : %r" 
          % (astr, bstr, is_permutation(astr, bstr)))

    astr = 'udita'; bstr = 'audit'
    print("%s is a permutation of %s : %r" 
          % (astr, bstr, is_permutation(astr, bstr)))

    astr = 'pompop'; bstr = 'oopmpo'
    print("%s is a permutation of %s : %r" 
          % (astr, bstr, is_permutation(astr, bstr)))

if __name__ == '__main__':
    run()
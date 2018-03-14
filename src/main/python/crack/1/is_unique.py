
def is_unique_with_ds(astr):
    '''
    use an extra data structure :  O(N)
    '''
    char_set = set()
    for c in astr :
        if c in char_set:
            return False
        else :
            char_set.add(c)

    return True

def is_unique_without_ds(astr):
    '''
    without using an extra data structure :  O(N^2)
    '''
    astr = sorted(astr)
    for i in range(0, len(astr)):
        for j in range(0, len(astr)):
            if(i != j and astr[i] == astr[j]):
                return False

    return True
                

def run():
    '''
    1.1 if a string has all unique characters
    '''
    astr = 'Udita'
    print("'%s' has unique characters : %r " % (astr, is_unique_without_ds(astr)))
    print("'%s' has unique characters : %r " % (astr, is_unique_with_ds(astr)))

    astr = 'Papa'
    print("'%s' has unique characters : %r " % (astr, is_unique_without_ds(astr)))
    print("'%s' has unique characters : %r " % (astr, is_unique_with_ds(astr)))

    astr = 'papa'
    print("'%s' has unique characters : %r " % (astr, is_unique_without_ds(astr)))
    print("'%s' has unique characters : %r " % (astr, is_unique_with_ds(astr)))

    astr = 'jobismeh'
    print("'%s' has unique char_set : %r " % (astr, is_unique_without_ds(astr)))
    print("'%s' has unique char_set : %r " % (astr, is_unique_with_ds(astr)))

if __name__ == '__main__':
    run()


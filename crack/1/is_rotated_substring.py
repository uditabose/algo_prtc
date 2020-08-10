def is_rotated_substring(astr, bstr):
    '''
    1.9 is one string rotated substring of other, O(N)
    '''
    big_string = "%s%s" % (bstr, bstr)
    return (astr in big_string)
        

def run():
    astr = "waterbottle"; bstr = "erbottlewat"
    print("%s is rotated subtring of %s : %r" 
          % (astr, bstr, is_rotated_substring(astr, bstr)))

if __name__ == '__main__':
    run()
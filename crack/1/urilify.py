
def urlify(astr, length):
    '''
    1.3 urlify a string, replace space with %20, O(N)
    '''
    tr_cnt = 0
    astr = astr.strip()
    if len(astr) != length:
        return "ERROR"

    bstr = ''
    for c in astr:
        if c == ' ':
            bstr += '%20'
        else :
            bstr += c

    return bstr

def run():
    astr = 'Mr John Smith   '; length = 13
    print("%s is urled as %s" % (astr, urlify(astr, length)))

    astr = '   Mr John Smith   '; length = 13
    print("%s is urled as %s" % (astr, urlify(astr, length)))

    astr = '   Mr John Smith'; length = 13
    print("%s is urled as %s" % (astr, urlify(astr, length)))


if __name__ == '__main__':
    run()

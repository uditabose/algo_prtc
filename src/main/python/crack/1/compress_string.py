
def compress_string(astr):
    '''
    1.6 compress the string
    '''
    old_char = astr[0]
    count = 0
    new_astr = ''
    for c in astr:
        if old_char == c:
            count += 1
        else:
            new_astr += old_char
            new_astr += str(count)
            old_char = c
            count = 1
    new_astr += old_char
    new_astr += str(count)

    if len(new_astr) >= len(astr):
        return astr
    else:
        return new_astr

def run():
    astr = 'aabcccccaaa'
    print("%s compressed to %s" % (astr, compress_string(astr)))

    astr = 'abcd'
    print("%s compressed to %s" % (astr, compress_string(astr)))

    astr = 'abbbccccddddd'
    print("%s compressed to %s" % (astr, compress_string(astr)))

if __name__ == '__main__':
    run()

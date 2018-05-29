import math

def one_edit_away_sort(astr, bstr):
    '''
    1.5 find if two strings are one or 
            less edits aways, via sort, O(Nlog(N))
    '''
    astr = sorted(astr.lower())
    bstr = sorted(bstr.lower())
    diff = [item for item in astr if item not in bstr]

    return (len(diff) <= 1)

def one_edit_away_dyn(astr, bstr):
    '''
    1.5 find if two strings are one or 
            less edits aways, via dynamic prog, O(N)
    '''
    if math.fabs(len(astr) - len(bstr)) > 1:
        return False

    ai = 0; bi = 0; ci = 0
    while ai < len(astr) and bi < len(bstr):
        if astr[ai] == bstr[bi]:
            ai += 1
            bi += 1
        elif astr[ai+1] == bstr[bi]:
            ai += 2
            bi += 1
            ci += 1
        elif astr[ai] == bstr[bi+1]:
            ai += 1
            bi += 2
            ci += 1
        else:
            ai += 1
            bi += 1
            ci += 1

    return (ci <= 1)

def run():
    astr = 'pale'; bstr = 'ple'
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_sort(astr, bstr)))
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_dyn(astr, bstr)))

    astr = 'pales'; bstr = 'pale'
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_sort(astr, bstr)))
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_dyn(astr, bstr)))

    astr = 'pale'; bstr = 'bale'
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_sort(astr, bstr)))
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_dyn(astr, bstr)))

    astr = 'pale'; bstr = 'bake'
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_sort(astr, bstr)))
    print("%s, %s -> %r" % (astr, bstr, one_edit_away_dyn(astr, bstr)))
    

if __name__ == '__main__':
    run()

def edit_distance(astr, bstr):
    if astr == None or len(astr) == 0:
        return 0

    if bstr == None or len(bstr) == 0:
        return 0

    edit_matrix = [[0] * len(astr) for n in range(len(bstr))]

    for i in range(0, len(astr)):
        for j in range(0, len(bstr)):
            if astr[i] == bstr[]:
                pass


if __name__ == '__main__':
    print(edit_distance('snowy', 'sunny'))
    print(edit_distance('potential', 'exponential'))
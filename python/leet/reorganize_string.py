
def reorganize_string(astr):
    '''
    Given a string S, check if the letters can be rearranged 
    so that two characters that are adjacent to each other 
    are not the same.

    If possible, output any possible result.  
    If not possible, return the empty string.
    https://leetcode.com/problems/reorganize-string/description/

    Time :
    Space:
    Note :
    '''
    chr_arr = [0] * 26
    for c in astr:
        chr_arr[c - 'a'] += 1

    sorted(chr_arr)

    for i in range(25, -1, -1):
        blanks = chr_arr[i] - 1

        if blanks <= 0:
            break
        
        for j in range(i - 1, -1):
            if blanks == 0:
                break

            if blanks >= chr_arr[j]:
                blanks -= chr_arr[j]
                chr_arr[j] = 0
            else:
                chr_arr[j] -= blanks
                blanks = 0

        sorted(chr_arr)

    return True if sum(chr_arr) <= 0 else False

def reorganizeString(S):
    N = len(S)
    A = []
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N+1)/2: return ""
        A.extend(c * x)
    ans = [None] * N
    ans[::2], ans[1::2] = A[N/2:], A[:N/2]
    return "".join(ans)

def run():
    astr = "aab"
    print(reorganizeString(astr))
    #print(reorganize_string(astr))

    astr = "aaab"
    print(reorganizeString(astr))
    #print(reorganize_string(astr))

if __name__ == '__main__':
    run()



def reverse_sub(astr, start, end):
    if start < 0 or end >= len(astr):
        return astr

    while start < end:
        astr[start], astr[end] = astr[end], astr[start]
        start += 1
        end -= 1

    return astr

def reverse_string_ii(astr, k):
    '''
    Given a string and an integer k, you need to reverse 
    the first k characters for every 2k characters counting 
    from the start of the string. If there are less than k 
    characters left, reverse all of them. If there are less 
    than 2k but greater than or equal to k characters, 
    then reverse the first k characters and left the other 
    as original.
    Example:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"
    
    Restrictions:
    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]

    https://leetcode.com/problems/reverse-string-ii/description/

    Time :
    Space:
    Note :
    '''
    if astr == None or len(astr) == 0:
        return astr

    if k < 1:
        return astr

    if len(astr) < k:
        return "".join(reverse_sub(list(astr), 0, len(astr)-1))

    start = 0
    as_list = list(astr)
    while start + k - 1 < len(as_list):
        astr = reverse_sub(as_list, start, start + k - 1) + as_list[start + k:]
        start = start + 2*k

    return "".join(as_list)

def run():
    print(reverse_string_ii("abcdefg", 2))
    #bacdfeg bacdfeg

    print(reverse_string_ii("abcd", 4))

if __name__ == '__main__':
    run()


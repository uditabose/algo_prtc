
def permutation_palindrome(astr):
    '''
    Write an efficient method that checks whether any 
    permutation ↴ of an input string is a palindrome. ↴

    You can assume the input string only contains 
    lowercase letters.

    Examples:

    "civic" should return true
    "ivicc" should return true
    "civil" should return false
    "livci" should return false

    https://www.interviewcake.com/question/java/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
    
    Time : O(N)
    Space: O(N)
    Note :
    '''
    chr_dict = {}
    for char in astr:
        if char in chr_dict:
            del chr_dict[char]
        else:
            chr_dict[char] = None
    
    return True if len(chr_dict) < 2 else False
        
def run():
    astr = 'civic'
    print("% s has palin : %s" % 
          (astr, str(permutation_palindrome(astr))))

    astr = 'ivicc'
    print("% s has palin : %s" % 
          (astr, str(permutation_palindrome(astr))))

    astr = 'civil'
    print("% s has palin : %s" % 
          (astr, str(permutation_palindrome(astr))))

    astr = 'livci'
    print("% s has palin : %s" % 
          (astr, str(permutation_palindrome(astr))))

if __name__ == '__main__':
    run()


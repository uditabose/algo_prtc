
mappings = {}
mappings['2'] = ['a', 'b', 'c']
mappings['3'] = ['d', 'e', 'f']
mappings['4'] = ['g', 'h', 'i']
mappings['5'] = ['j', 'k', 'l']
mappings['6'] = ['m', 'n', 'o']
mappings['7'] = ['p', 'q', 'r', 's']
mappings['8'] = ['t', 'u', 'v']
mappings['9'] = ['w', 'y', 'x', 'z']

def get_all_options(num_str, curr_idx, option_arr):
    if curr_idx == len(num_str):
        return option_arr

    curr_char = num_str[curr_idx]
    temp_arr = []
    print(option_arr)
    print(curr_char)
    for opt in option_arr:
        for mp in mappings[curr_char]:
            temp_arr.append(opt + mp)

    return get_all_options(num_str, curr_idx + 1, temp_arr)

        
def letter_combinations_of_a_phone_number(num):
    '''
    Given a string containing digits from 2-9 inclusive, 
    return all possible letter combinations that the number 
    could represent.

    A mapping of digit to letters (just like on the telephone buttons) 
    is given below. Note that 1 does not map to any letters.

    Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
    
    Time : O(N*K)
    Space: O(N*K)
    Note :
    recursively add a character
    1. pick character at index i
    2. create possibilities by appending alpha chars 
        to all existing options
    3. if i == len(str) - 1, return array
    '''
    if num < 2:
        return []

    num_str = str(num)
    return get_all_options(num_str, 0, [""])

def run():
    num = 23
    print(letter_combinations_of_a_phone_number(num))

    #num = 23678
    #print(letter_combinations_of_a_phone_number(num))

if __name__ == '__main__':
    run()



def output_contest_matches(no_of_teams):
    '''
    During the NBA playoffs, we always arrange the rather strong team 
    to play with the rather weak team, like make the rank 1 
    team play with the rank nth team, which is a good strategy 
    to make the contest more interesting. Now, you're given n teams, 
    you need to output their final contest matches in the form of a 
    string.

    The n teams are given in the form of positive integers 
    from 1 to n, which represents their initial rank. 
    (Rank 1 is the strongest team and Rank n is the weakest team.) 
    We'll use parentheses('(', ')') and commas(',') to represent 
    the contest team pairing - parentheses('(' , ')') for pairing 
    and commas(',') for partition. During the pairing process in 
    each round, you always need to follow the strategy of making 
    the rather strong one pair with the rather weak one.

    Example 1:
    Input: 2
    Output: (1,2)
    Explanation: 
    Initially, we have the team 1 and the team 2, placed like: 1,2.
    Then we pair the team (1,2) together with '(', ')' and ',', 
    which is the final answer.
    
    Example 2:
    Input: 4
    Output: ((1,4),(2,3))
    Explanation: 
    In the first round, we pair the team 1 and 4, the team 2 and 3 
    together, as we need to make the strong team and weak team together.
    And we got (1,4),(2,3).
    In the second round, the winners of (1,4) and (2,3) need 
    to play again to generate the final winner, so you need to 
    add the parentheses outside them.
    And we got the final answer ((1,4),(2,3)).
    
    Example 3:
    Input: 8
    Output: (((1,8),(4,5)),((2,7),(3,6)))
    Explanation: 
    First round: (1,8),(2,7),(3,6),(4,5)
    Second round: ((1,8),(4,5)),((2,7),(3,6))
    Third round: (((1,8),(4,5)),((2,7),(3,6)))
    Since the third round will generate the final winner, 
    you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
    
    Note:
    The n is in range [2, 212].
    We ensure that the input n can be converted into the form 2k, 
    where k is a positive integer.

    https://leetcode.com/problems/output-contest-matches/description/

    Time : O(N2)
    Space: O(N)
    Note :
    1. create a match array with all numbers in range
    2. loop over match array
    3. inside loop with 2 indices, one from left-end, another
        from right end
    4. fill out the array with match
    5. continue till match array length is one (1)
    6. return the first element as string
    '''
    if no_of_teams < 2:
        return '()'

    match_arr = [idx for idx in range(1, no_of_teams+1)]
    
    while len(match_arr) > 1:
        i = 0
        j = len(match_arr) - 1
        temp_arr = []
        while i < j:
            temp_arr.append((match_arr[i], match_arr[j]))
            i += 1
            j -= 1

        match_arr = temp_arr

    return str(match_arr[0]).replace(' ', '')

def run():
    no_of_teams = 2
    print("teams %s" % output_contest_matches(no_of_teams))

    no_of_teams = 4
    print("teams %s" % output_contest_matches(no_of_teams))

    no_of_teams = 8
    print("teams %s" % output_contest_matches(no_of_teams))

    no_of_teams = 4096
    print("teams %s" % output_contest_matches(no_of_teams))

if __name__ == '__main__':
    run()


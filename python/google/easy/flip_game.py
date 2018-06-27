
def flip_game(game_str):
    '''
    You are playing the following Flip Game with your 
    friend: Given a string that contains only these two 
    characters: + and -, you and your friend take turns to 
    flip two consecutive "++" into "--". The game ends when 
    a person can no longer make a move and therefore the other 
    person will be the winner.

    Write a function to compute all possible states of the 
    string after one valid move.

    Example:

    Input: s = "++++"
    Output: 
    [
      "--++",
      "+--+",
      "++--"
    ]
    Note: If there is no valid move, return an empty list [].

    https://leetcode.com/problems/flip-game/description/

    Time : O(N)
    Space: O(NC2), number of combinationss
    Note :
    1. take 2 indices, start, end; end = start + 2
    2. move by 2
    3. if substring (start, end) is `++` then flip to `--`
    4. add that option to return array
    '''
    if game_str == None or len(game_str) < 2:
        return []

    possible_moves = []
    for start in range(0, len(game_str)):
        end = start + 2
        if game_str[start:end] == '++':
            opt = game_str[0:start] + '--' + game_str[end:]
            possible_moves.append(opt)

    return possible_moves  

def run():
    game_str = '+'
    print(flip_game(game_str))

    game_str = '++'
    print(flip_game(game_str))

    game_str = '----'
    print(flip_game(game_str))

    game_str = '++++'
    print(flip_game(game_str))

    game_str = '+++--+++-'
    print(flip_game(game_str))


if __name__ == '__main__':
    run()


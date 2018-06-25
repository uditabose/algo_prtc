
def judge_route_circle(route):
    '''
    Initially, there is a Robot at position (0, 0). 
    Given a sequence of its moves, judge if this robot 
    makes a circle, which means it moves back to the original place.

    The move sequence is represented by a string. 
    And each move is represent by a character. The valid 
    robot moves are R (Right), L (Left), U (Up) and D (down). 
    The output should be true or false representing whether 
    the robot makes a circle.

    Example 1:
    Input: "UD"
    Output: true
    
    Example 2:
    Input: "LL"
    Output: false

    https://leetcode.com/problems/judge-route-circle/description/

    Time : O(N)
    Space: O(1)
    Note :
    1. take 2 var, right-count, up-count
    2. increase corresponding count on right or up
    3. decrease corresponding count on left or down
    4. if sum of right-count and up-count is zero, 
        return true, else false
    '''
    if route == None or len(route) == 0:
        return True

    right = 0
    up = 0

    for r in route:
        if r == 'R':
            right += 1
        elif r == 'U':
            up += 1
        elif r == 'L':
            right -= 1
        elif r == 'D':
            up -= 1

    return (right + up) == 0

def run():
    route = 'UD'
    print("circles back %s" % str(judge_route_circle(route)))

    route = 'LL'
    print("circles back %s" % str(judge_route_circle(route)))

if __name__ == '__main__':
    run()


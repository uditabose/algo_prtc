
def paint_fence(fences, colors):
    '''
    There is a fence with n posts, each post can be 
    painted with one of the k colors.

    You have to paint all the posts such that no 
    more than two adjacent fence posts have the same color.

    Return the total number of ways you can paint the fence.

    Note:
    n and k are non-negative integers.

    Example:

    Input: n = 3, k = 2
    Output: 6
    Explanation: Take c1 as color 1, c2 as color 2. 
    All possible ways are:

                post1  post2  post3      
     -----      -----  -----  -----       
       1         c1     c1     c2 
       2         c1     c2     c1 
       3         c1     c2     c2 
       4         c2     c1     c1  
       5         c2     c1     c2
       6         c2     c2     c1
    https://leetcode.com/problems/paint-fence/description/
    
    Time :
    Space:
    Note :

    tn = total possibilities for nth choice
    k = number of colors

    t0 = 0
    t1 = k
    t2 = k*1 (same colors as last one) + k*(k-1) (different colors for each)
    t3 = t2 + t1*(k-1) (diff from last)
    t4 = t3 (same as last) + t2*(k-1) (diff from last)
    ...
    ...
    tn = t(n-1) + t(n-2)*(k-1)
    '''
    if fences == 0:
        return 0
    if fences == 1:
        return colors

    same_color = colors # for n=2
    diff_colors = colors * (colors - 1) # for n=2

    for x in range(2, fences):
        temp = diff_colors
        diff_colors = (same_color + diff_colors)*(colors - 1)
        same_color = temp

    return (same_color + diff_colors)

def run():
    print("paint options : %d" % paint_fence(1, 5))
    print("paint options : %d" % paint_fence(3, 2))
    print("paint options : %d" % paint_fence(3, 5))
    print("paint options : %d" % paint_fence(10, 5))

if __name__ == '__main__':
    run()


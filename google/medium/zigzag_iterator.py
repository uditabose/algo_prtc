
class ZigzagIterator(object):
    '''
    
    Given two 1d vectors, implement an iterator to 
    return their elements alternately.

    Example:

    Input:
    v1 = [1,2]
    v2 = [3,4,5,6] 

    Output: [1,3,2,4,5,6]

    Explanation: By calling next repeatedly until 
            hasNext returns false, 
            the order of elements returned by next should be: 
            [1,3,2,4,5,6].
    Follow up: What if you are given k 1d vectors? 
            How well can your code be extended to such cases?

    Clarification for the follow up question:
    The "Zigzag" order is not clearly defined and 
    is ambiguous for k > 2 cases. If "Zigzag" does not 
    look right to you, replace "Zigzag" with "Cyclic". For example:

    Input:
    [4,5,6,7]
    [8,9]
    [1,2,3]
    
    
    #[8,2,5,1]

    Output: [1,4,8,2,5,9,3,6,7].

    https://leetcode.com/problems/zigzag-iterator/description/

    Time :
    Space:
    Note :
    '''

    def __init__(self, vectors):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        
        if vectors == None or len(vectors) == 0:
            raise ValueError("invalid vectors") 

        self.vectors = vectors
        self.pos_arr = [(idx, 0, len(vec)) for idx, vec in enumerate(vectors)]
        self.curr_idx = 0
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            curr_vec = self.pos_arr[self.curr_idx]
            curr_val = self.vectors[curr_vec[0]][curr_vec[1]]
            self.update_next()
            return curr_val

    def update_next(self):
        if self.pos_arr == None or len(self.pos_arr) == 0:
            self.curr_idx = None
            return

        if self.curr_idx >= len(self.pos_arr):
            self.curr_idx = None
            return

        curr_vec = self.pos_arr[self.curr_idx]

        if curr_vec[1] < curr_vec[2]:            
            if curr_vec[1] + 1 < curr_vec[2]:
                self.pos_arr[self.curr_idx] = (curr_vec[0], curr_vec[1] + 1, curr_vec[2])
                self.curr_idx = (self.curr_idx + 1) % len(self.pos_arr)
            else:
                self.pos_arr.pop(self.curr_idx)
                if len(self.pos_arr) > 0:
                    self.curr_idx = self.curr_idx % len(self.pos_arr)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pos_arr == None or len(self.pos_arr) == 0:
            return False

        if self.curr_idx == None or self.curr_idx >= len(self.pos_arr):
            return False

        curr_vec = self.pos_arr[self.curr_idx]

        if curr_vec[1] < curr_vec[2]:
            return True
        else:            
            return False

def run():
    zz_iter = ZigzagIterator([[1,2], [3,4,5,6]])
    vals = []
    while zz_iter.hasNext():
        vals.append(zz_iter.next())
    print(vals)
    # [1,3,2,4,5,6]
    # [1, 3, 2, 4, 5, 6]

    zz_iter = ZigzagIterator([[1,2,3], [4,5,6,7], [8,9]])
    vals = []
    while zz_iter.hasNext():
        vals.append(zz_iter.next())
    print(vals)
    # [1,4,8,2,5,9,3,6,7]
    # [1, 4, 8, 2, 5, 9, 3, 6, 7]

    
    
    #[8,2,5,1]


if __name__ == '__main__':
    run()


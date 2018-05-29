
import random

def shuffle_combinatorics_probability_math(stuff_list):
    '''
    Write a function for doing an in-place ↴ shuffle of a list.

    The shuffle must be "uniform," meaning each item in the 
    original list must have the same probability of ending 
    up in each spot in the final list.

    https://www.interviewcake.com/question/python/shuffle?course=fc1&section=combinatorics-probability-math
    
    Time : O(N)-ish. Random number generation can become a 
            multiplier effect

    Space : O(N)
    Note: random number generation issue
    '''
    length = len(stuff_list)
    from_idx = random.randint(0, length - 1)
    to_idx = random.randint(0, length - 1)
    from_value = stuff_list[from_idx]

    from_idx_arr = [1 for i in range(0, length)]

    # picks a random int for from, and for to
    # if the indices are same, garbage loop
    # otherwise, store the to-value in temp var
    # replace to-index with from-value
    # use the current to-idx, temp for next round from
    # calculate to-idx
    # flip the array position, so to never replace same index twice
    while sum(from_idx_arr) > 0:
        #print("[%d](%s) to [%d](%s)" 
         #     % (from_idx, str(from_value), to_idx, str(stuff_list[to_idx])))
        
        # if the idices are same, then have to loop again
        if from_idx == to_idx:
            to_idx = random.randint(0, length - 1)
        else:
            to_value = stuff_list[to_idx] # old to-place value, next round from 
            stuff_list[to_idx] = from_value # replace with from value
            from_value = to_value # next-round value
            from_idx_arr[from_idx] = 0 # flip the index
            from_idx = to_idx # next roung from index
            to_idx = random.randint(0, length - 1) # next-round to


if __name__ == '__main__':
    stuff_list = [10, 50, 29, 56, 2, 98, 400]
    print(stuff_list)
    shuffle_combinatorics_probability_math(stuff_list)
    print(stuff_list)

    stuff_list = ['ami', 'papa', 'buba', 'puchi', 'madhu', 'phulkai']
    print(stuff_list)
    shuffle_combinatorics_probability_math(stuff_list)
    print(stuff_list)



            

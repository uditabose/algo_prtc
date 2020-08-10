
def count_ways(no_of_stairs, steps_map):
    if no_of_stairs <= 0:
        return 0
    elif no_of_stairs == 1:
        return 1

    if no_of_stairs in steps_map:
        return steps_map[no_of_stairs]
    else:
        ways = 1 + (count_ways(no_of_stairs - 1, steps_map) 
                    + count_ways(no_of_stairs - 2, steps_map) 
                    + count_ways(no_of_stairs - 3, steps_map))
        steps_map[no_of_stairs] = ways

        return ways
    
def triple_step(no_of_stairs):
    '''
    8.1 a child can hop 1, 2 or 3 steps at a time.
    count how many possible ways child can run up `n`
    steps.

    Time : O(N)
    Space: O(N)
    Note : if memoization used the time is O(N) otherwise O(N!)
    '''

    if no_of_stairs < 2:
        return 1

    no_of_ways = {}
    ways = count_ways(no_of_stairs, no_of_ways)

    return ways

def run():
    no_of_stairs = 0
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

    no_of_stairs = 1
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

    no_of_stairs = 2
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

    no_of_stairs = 3
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

    no_of_stairs = 10
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

    no_of_stairs = 32
    print("%d steps in %d ways" 
          % (no_of_stairs, triple_step(no_of_stairs)))

if __name__ == '__main__':
    run()


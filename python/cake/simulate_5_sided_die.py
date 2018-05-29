
import random

def rand7():
    return random.randint(1, 7)

def rand5():
    return int((rand7() * 5) / 7)

def simulate_5_sided_die():
    '''
    You have a function rand7() that generates a 
    random integer from 1 to 7. Use it to write a 
    function rand5() that generates a random integer from 1 to 5.

    rand7() returns each integer with equal probability. 
    rand5() must also return each integer with equal probability.

    https://www.interviewcake.com/question/python/simulate-5-sided-die?course=fc1&section=combinatorics-probability-math
    
    Time : O(1)
    Space : O(1)
    Note : it's not equal-probability, see the worked out answer
    Time could go O(inf)
    '''
    return rand5()

if __name__ == "__main__":
    print("Rand 1 : %d" % simulate_5_sided_die())
    print("Rand 2 : %d" % simulate_5_sided_die())
    print("Rand 3 : %d" % simulate_5_sided_die())
    print("Rand 4 : %d" % simulate_5_sided_die())
    print("Rand 5 : %d" % simulate_5_sided_die())
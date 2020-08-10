
import random

def rand5():
    return random.randint(1, 5)

def simulate_7_sided_die():
    '''
    You have a function rand5() that generates a random 
    integer from 1 to 5. Use it to write a function rand7() 
    that generates a random integer from 1 to 7.

    rand5() returns each integer with equal probability. 
    rand7() must also return each integer with equal probability.
    
    https://www.interviewcake.com/question/python/simulate-7-sided-die?section=combinatorics-probability-math&course=fc1

    Time : O(inf)
    Space : O(1)
    '''
    mult = rand5() * rand5()
    while True:
        if mult <= 7:
            return mult
        else:
            mult = rand5() * rand5()
        

if __name__ == '__main__':

    for x in range(1,10):
        print("rand %d : %d" % (x, simulate_7_sided_die()))
    

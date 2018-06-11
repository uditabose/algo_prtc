
def top_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    '''
    You created a game that is more popular than Angry Birds.

    Each round, players receive a score between 0 and 100, 
    which you use to rank them from highest to lowest. 
    So far you're using an algorithm that sorts in 
    O(nlg{n})O(nlgn) time, but players are complaining that 
    their rankings aren't updated fast enough. You need a 
    faster sorting algorithm.

    Write a function that takes:

    a list of unsorted_scores
    the highest_possible_score in the game
    and returns a sorted list of scores in less than 
    O(nlg{n})O(nlgn) time.

    Time : O(N)
    Space: O(N+m), m = highest possible score
    Note : won't be as good if highest score is in millions
    '''
    highest_bit_arr = [0] * (HIGHEST_POSSIBLE_SCORE + 1)
    for x in unsorted_scores:
        highest_bit_arr[x] = 1

    sorted_arr = []
    for x in range(HIGHEST_POSSIBLE_SCORE, -1, -1):
        if highest_bit_arr[x] == 1:
            sorted_arr.append(x)

    return sorted_arr

def run():
    unsorted_scores = [37, 89, 41, 65, 91, 53]
    HIGHEST_POSSIBLE_SCORE = 100

    # Returns [91, 89, 65, 53, 41, 37]
    sorted_score = top_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
    print(unsorted_scores)
    print(sorted_score)

if __name__ == '__main__':
    run()


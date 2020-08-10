def merging_ranges(range_tuple):
    '''
    https://www.interviewcake.com/question/python/merging-ranges

    sort the start times, sort the end times, 
    if last end time is less than or equals to next start time
    then update the last end time with next time, this is a merged
    range.
    otherwise start a new range.
    '''
    start_times, end_times = sorted([x for (x,y) in range_tuple]), sorted([y for (x,y) in range_tuple])
    compressed_range = [[start_times[0], end_times[0]]]

    for i in xrange(1,len(range_tuple)):
        if compressed_range[-1][1] < start_times[i]:
            compressed_range.append([start_times[i], end_times[i]])
        else :
            compressed_range[-1][1] = end_times[i]

    return compressed_range

if __name__ == '__main__':
    compressed_range = merging_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    print(compressed_range)

    compressed_range = merging_ranges([(0, 1), (3, 5), (6, 8), (10, 12), (9, 11)])
    print(compressed_range)

    compressed_range = merging_ranges([(1, 2), (2, 3)])
    print(compressed_range)

    compressed_range = merging_ranges([(1, 5), (2, 3)])
    print(compressed_range)

    compressed_range = merging_ranges([(1, 10), (2, 6), (3, 5), (7, 9)])
    print(compressed_range)

      

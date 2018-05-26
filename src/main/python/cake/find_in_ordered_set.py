
#from math import abs
def find_in_ordered_set(ordered_list, num):
    '''
    Suppose we had a list ↴ of nn integers sorted in 
    ascending order. How quickly could we check if a 
    given integer is in the list?

    https://www.interviewcake.com/question/python/find-in-ordered-set?course=fc1&section=combinatorics-probability-math
    
    Time  : O(logN)
    Space : O(1)
    Notes : 
    '''
    if ordered_list == None or len(ordered_list) == 0 :
        return False

    if ordered_list[0] > num or ordered_list[-1] < num:
        return False

    mid = int(len(ordered_list)/2) # mid index of list
    start = 0                      # start index of list
    end = len(ordered_list)        # end index of list

    while mid >= start and mid < end:
        #print("begin :: start[%d] :: mid[%d] :: end[%d]" % (start, mid, end))
        
        if ordered_list[mid] == num: # matches with mid
            return True
        elif end <= start: # something wrong
            return False   
        else:
            # if distance between start and end index is 
            # 1 (one), then the mid calculation will infinitely
            # dance between the two numbers, and the loop would
            # finally throw a stack overflow exception
            #
            # so, in this case the chosen number is between 
            # start and end, and doesn't match either
            # hence number is not there
            if abs(end - start) == 1: 
                if ordered_list[end] == num or ordered_list[start] == num:
                    return True
                else :
                    return False
        
            if ordered_list[mid] > num:
                end = mid
            else:
                start = mid
            mid = start + int((end - start)/2)

        #print("end :: start[%d] :: mid[%d] :: end[%d]" % (start, mid, end))

    return False


if __name__ == '__main__':
    
    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 50
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 70
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 20
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 90
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 10
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 100
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 5
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 15
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    num = 85
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     
    
    

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 50
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 70
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 20
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 90
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 10
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 100
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 5
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 15
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
    num = 85
    print("%d is in %s = %s\n" % (num, ordered_list, str(find_in_ordered_set(ordered_list, num))))     

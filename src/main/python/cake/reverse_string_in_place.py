

def swap(astr_list, left, right):
    l_val = astr_list[left]
    r_val = astr_list[right]

    astr_list[left] = r_val
    astr_list[right] = l_val

def reverse_string_in_place(astr_list):
    '''
    Write a function that takes a list of characters 
    and reverses the letters in-place. 
    
    https://www.interviewcake.com/question/python/reverse-string-in-place?section=array-and-string-manipulation&course=fc1

    Time : O(N)
    Space : O(1)
    '''
    left = 0
    right = len(astr_list) - 1
    while left < right:
        #swap(astr_list, left, right)
        astr_list[left], astr[right] = astr[right], astr_list[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    astr = list("This is a string")
    print(astr)
    reverse_string_in_place(astr)
    print(astr)
    print("")

    astr = list("papa")
    print(astr)
    reverse_string_in_place(astr)
    print(astr)
    print("")

    astr = list("Udita")
    print(astr)
    reverse_string_in_place(astr)
    print(astr)
    print("")
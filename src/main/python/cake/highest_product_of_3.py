def highest_product_of_3_via_sort_no_negative(list_of_ints) :
    '''
    https://www.interviewcake.com/question/python/highest-product-of-3
    :param list_of_ints:
    :return:
    '''
    sorted_ints = sorted(list_of_ints, reverse=True)

    return sorted_ints[0] * sorted_ints[1] * sorted_ints[2]

def highest_product_of_3(list_of_ints) :
    '''
    https://www.interviewcake.com/question/python/highest-product-of-3
    :param list_of_ints:
    :return:
    '''
    sorted_ints = sorted(list_of_ints, reverse=True)




if __name__ == '__main__':
    print ("Sorted %d : " % highest_product_of_3_via_sort_no_negative([2, 1, 66.25, 333, 333, 1234]))

import unittest

def highest_product_of_3_via_sort_no_negative(list_of_ints) :
    '''
    https://www.interviewcake.com/question/python/highest-product-of-3
    
    Given a list of integers, find the highest product 
    you can get from three of the integers.

    The input list_of_ints will always have at least 
    three integers.
    
    :param list_of_ints:
    :return:
    '''
    sorted_ints = sorted(list_of_ints, reverse=True)

    return sorted_ints[0] * sorted_ints[1] * sorted_ints[2]

def highest_product_of_3(list_of_ints) :
    '''
    https://www.interviewcake.com/question/python/highest-product-of-3
    
    Given a list of integers, find the highest product 
    you can get from three of the integers.

    The input list_of_ints will always have at least 
    three integers.

    :param list_of_ints:
    :return:
    '''
    if list_of_ints == None or len(list_of_ints) < 3:
        raise Exception()

    current_max_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    current_max_2 = list_of_ints[0] * list_of_ints[1]
    current_min_2 = list_of_ints[0] * list_of_ints[1]
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])

    for x in list_of_ints[2:]:

        current_max_3 = max(current_max_3,
                            current_max_2 * x,
                            current_min_2 * x)

        current_max_2 = max(current_max_2, 
                            highest * x,
                            lowest * x)
        
        current_min_2 = min(current_min_2, 
                            highest * x,
                            lowest * x)

        highest = max(highest, x)

        lowest = min(lowest, x)

    return current_max_3

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)

#if __name__ == '__main__':
#    print ("Sorted %d : " % highest_product_of_3_via_sort_no_negative([2, 1, 66.25, 333, 333, 1234]))
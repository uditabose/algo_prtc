def product_of_other_numbers_with_division(numbers):
    '''
    https://www.interviewcake.com/question/python/product-of-other-numbers
    :param numbers:
    :return:
    '''
    all_mult = reduce(lambda x, y : x * y, numbers)
    i = 0
    while i < len(numbers):
        numbers[i] = all_mult / numbers[i]
        i += 1

    return numbers

def product_of_other_numbers_no_division(numbers):
    '''
    https://www.interviewcake.com/question/python/product-of-other-numbers
    :param numbers:
    :return:
    '''
    left_product = 1
    product = [1] * len(numbers)
    i = 0
    while i < len(numbers):
        product[i] = left_product
        left_product *= numbers[i]
        i += 1

    right_product = 1
    i = len(numbers) - 1
    while i > -1:
        product[i] *= right_product
        right_product *= numbers[i]
        i -= 1
    return product

if __name__ == '__main__':
    print("Other %s" % product_of_other_numbers_with_division([1, 7, 3, 4]))
    print("Other %s" % product_of_other_numbers_no_division([1, 7, 3, 4]))

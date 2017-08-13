def product_of_other_numbers_with_division(numbers):
    all_mult = reduce(lambda x, y : x * y, numbers)
    i = 0
    while i < len(numbers):
        numbers[i] = all_mult / numbers[i]
        i += 1

    return numbers

def product_of_other_numbers_no_division(numbers):
    

if __name__ == '__main__':
    print("Other %s" % product_of_other_numbers_with_division([1, 7, 3, 4]))

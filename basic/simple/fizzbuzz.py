
def fizzbuzz(num):
    if num <= 1:
        return [num]

    ret_arr = []
    for i in range(1, num+1):
        if i % 15 == 0:
            ret_arr.append('FizzBuzz')
        elif i % 5 == 0:
            ret_arr.append('Buzz')
        elif i % 3 == 0:
            ret_arr.append('Fizz')
        else:
            ret_arr.append(i)
        

    return ret_arr

if __name__ == '__main__':
    print(fizzbuzz(100))



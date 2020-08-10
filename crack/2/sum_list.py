import sys
sys.path.append('./ds/')

from linked_list import LinkedList

def sum_list_reverse(num1, num2):
    '''
    2.5 sum up two list, reversed input, O(N)
    https://leetcode.com/problems/add-two-numbers/description/
    '''
    summed = LinkedList()
    carry = 0
    n1 = num1.get_head()
    n2 = num2.get_head()
    while n1 != None or n2 != None:
        summ = carry + n1.get_data() + n2.get_data()
        if summ >= 10:
            summed.insert(summ - 10)
            carry = 1
        else:
            summed.insert(summ)
        n1 = n1.get_next()
        n2 = n2.get_next()

    rest = n1 if n1 != None else n2
    while rest != None:
        summ = carry + rest.get_data()
        if summ >= 10:
            summed.insert(summ - 10)
            carry = 1
        else:
            summed.insert(summ)
        rest = rest.get_next()
    return summed

def sum_list(num1, num2):
    '''
    2.5 sum up two list, O(N)
    '''

    n1 = num1.get_head()
    n2 = num2.get_head()
    n1str = ""
    n2str = ""
    while n1 != None:
        n1str += str(n1.get_data())
        n1 = n1.get_next()

    while n2 != None:
        n2str += str(n2.get_data())
        n2 = n2.get_next()

    sumstr = str(int(n1str) + int(n2str))
    summed = LinkedList()
    for c in sumstr:
        summed.insert(c)

    return summed

def run():
   list1 = [7, 1, 6]
   list2 = [5, 9, 2]
   num1 = LinkedList()
   num2 = LinkedList()
   num1.build(list1)
   num2.build(list2)

   summed = sum_list_reverse(num1, num2)
   print(summed)

   list1 = [6, 1, 7]
   list2 = [2, 9, 5]
   num1 = LinkedList()
   num2 = LinkedList()
   num1.build(list1)
   num2.build(list2)

   summed = sum_list(num1, num2)
   print(summed)

if __name__ == '__main__':
    run()


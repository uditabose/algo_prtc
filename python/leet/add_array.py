# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

    def __repr__(self):
        lstr = ""
        curr = self
        while curr != None:
            lstr += str(curr.val)
            lstr += " "
            curr = curr.next

        return lstr

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            raise ValueError('empty list')

        carry = 0
        n1 = l1
        n2 = l2
        n3 = None
        l3 = None
        while n1 != None and n2 != None:
            
            summed = carry + n1.val + n2.val
            carry = int(summed / 10)
            summed = summed % 10
            
            if n3 == None:
                n3 = ListNode(summed)
                l3 = n3
            else:
                n3.next = ListNode(summed)
                n3 = n3.next
                                
            n1 = n1.next
            n2 = n2.next
            
        while n1 != None:
            summed = carry + n1.val
            carry = int(summed / 10)
            summed = summed % 10

            n3.next = ListNode(summed)
            n3 = n3.next
                    
            n1 = n1.next

        while n2 != None:
            summed = carry + n2.val
            carry = int(summed / 10)
            summed = summed % 10

            n3.next = ListNode(summed)
            n3 = n3.next
                    
            n2 = n2.next

        if carry != 0:
            n3.next = ListNode(carry)
            
        return l3

if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(9)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(1)
    l2.next.next.next = ListNode(1)
    print(sol.addTwoNumbers(l1, l2))
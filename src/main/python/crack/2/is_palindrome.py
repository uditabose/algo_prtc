import sys
sys.path.append('./ds/')

from linked_list import LinkedList

def is_palindrome(linked_list):
    '''
    2.6 find if list is palindrome, O(N)
    '''
    reversed = LinkedList()
    curr_node = linked_list.get_head()
    to_end = ""
    from_end = ""
    while curr_node != None:
        to_end += curr_node.get_data()
        from_end = curr_node.get_data() + from_end
        curr_node = curr_node.get_next()

    return to_end == from_end

def run():
    base_list = ['n', 'o', 't', 'z', 'o', 'z', 'g', 'q', 'm']
    link_list = LinkedList()
    link_list.build(base_list)
    print(link_list)
    if is_palindrome(link_list):
        print("It's a palindrome")
    else:
        print("It's NOT a palindrome")
        
    
    base_list = ['m', 'q', 'g', 'z', 'o', 'z', 'g', 'q', 'm']
    link_list = LinkedList()
    link_list.build(base_list)
    print(link_list)
    if is_palindrome(link_list):
        print("It's a palindrome")
    else:
        print("It's NOT a palindrome")

if __name__ == '__main__':
    run()


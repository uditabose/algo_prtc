
import sys
sys.path.append('./ds/')

from linked_list import linked_list


def remove_dupes_buffer(link_list):
    '''
    2.1 remove dupes, with buffer, 
        time :O(N), additional space : O(N)
        DOESN'T WORK
    '''
    if link_list == None:
        return None

    non_dupes = set()
    curr_node = link_list
    while curr_node != None:
        data = curr_node.get_data()
        non_dupes.add(data)  
        curr_node = curr_node.get_next()

    return list(non_dupes)

def remove_node(link_list, node):
    if link_list == None or node == None:
        return None

    curr_node = link_list
    prev_node = None
    next_node = None
    while curr_node != None:
        if curr_node == node:
            next_node = curr_node.get_next()
            break
        else:
            prev_node = curr_node
            next_node = curr_node.get_next()
        curr_node = curr_node.get_next()

    if prev_node == None:
        return next_node
    else:
        prev_node.set_next(next_node)
        return prev_node

def remove_dupes_no_buffer(link_list):
    '''
    2.1 remove dupes, without buffer, 
        time :O(N^2), additional space : none
    '''
    if link_list == None:
        return

    curr_node = link_list
    while curr_node != None:
        data = curr_node.get_data()
        if data == None :
            break

        next_node = curr_node.get_next()
        while next_node != None:
            if data == next_node.get_data():
                next_node.set_data()
            next_node = next_node.get_next()
        curr_node = curr_node.get_next()

    curr_node = link_list
    while curr_node != None:
        data = curr_node.get_data()
        if data == None :
            remove_node(link_list, curr_node)

        curr_node = curr_node.get_next()

def run():
   dupes_list = ['m', 'q', 'g', 'z', 'o', 'a', 'u', 'e', 'a', 'm', 's']
   dupes_ll = linked_list()
   
   for e in dupes_list[1:]:
       dupes_ll.set_data(e)
       dupes_ll.set_next(linked_list())
       dupes_ll = dupes_ll.get_next()
   
   non_dupes = remove_dupes_buffer(dupes_ll)
   print("%s\n-------------\n" % non_dupes)

   dupes_ll = linked_list(dupes_list[0])
   
   for e in dupes_list[1:]:
       new_node = linked_list(e)
       dupes_ll.set_next(new_node)
       dupes_ll = new_node

   non_dupes = remove_dupes_no_buffer(dupes_ll)
   print("%s\n-------------\n" % non_dupes)
   

if __name__ == '__main__':
    run()


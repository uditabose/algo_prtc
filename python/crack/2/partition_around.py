import sys
sys.path.append('./ds/')

from linked_list import LinkedList

def partition_around(link_list, part_val):

    '''
    2.4 partition around the value, O(N)
    '''
    curr_node = link_list.get_head()
    part_list = LinkedList()
    while curr_node != None:
        #print(curr_node)
        data = curr_node.get_data()
        if data == None:
            break
        if data >= part_val:
            part_list.insert(data)
        elif data < part_val:
            part_list.insert_head(data)

        curr_node = curr_node.get_next()

    return part_list

def run():
    base_list = [3, 5, 8, 5, 10, 2, 1]
    link_list = LinkedList()
    link_list.build(base_list)
    print(link_list)

    part_list = partition_around(link_list, 5)
    print(part_list)


if __name__ == '__main__':
    run()


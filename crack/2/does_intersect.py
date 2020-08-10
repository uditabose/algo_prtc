import sys
sys.path.append('./ds/')

from linked_list import LinkedList

def does_intersect(list1, list2):
    '''
    2.7 does two lists intersect, O(N)
    '''
    node_set = set()
    curr_node = list1.get_head()
    while curr_node != None:
        node_set.add(curr_node)
        curr_node = curr_node.get_next()

    curr_node = list2.get_head()
    while curr_node != None:
        if curr_node in node_set:
            return curr_node
        else:
            node_set.add(curr_node)
        curr_node = curr_node.get_next()

    return None

def run():
    base_list = ['n', 'o', 't', 'z', 'o', 'z', 'g', 'q', 'm']
    list1 = LinkedList()
    list1.build(base_list)

    list2 = LinkedList()
    list2.build(['z', 'g', 'q'])
    list2.get_last().set_next(list1.get_head())

    print(list1)
    print(list2)
    doesit = does_intersect(list2, list1)


    if doesit == None:
        print("NO")
    else:
        print("YES : %s" % doesit.get_data())

if __name__ == '__main__':
    run()



import sys
sys.path.append('./ds/')

from linked_list import linked_list

def delete_middle(link_list):
   '''
    2.3 delete middle element, O(N)
   '''
   slow_node = link_list
   fast_node = link_list

   while fast_node != None:
       slow_node = slow_node.get_next()
       fast_node = fast_node.get_next().get_next()

   link_list.delete_node(slow_node)
   return link_list

def run():
   base_list = ['m', 'q', 'g', 'z', 'o', 'a', 'u', 'e', 'a', 'm', 's']
   link_list = linked_list()
   link_list.build(base_list)
   print(link_list)

   link_list = delete_middle(link_list)
   print(link_list)

if __name__ == '__main__':
    run()

